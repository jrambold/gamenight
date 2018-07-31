from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from events.models import Player, UserEvent, FriendRequest, NewMemberRequest
from events.forms import SignUpForm, UserEventForm, AddFriendForm, AcceptFriendForm
from events.utils import welcome_email, new_event_email, friend_invite_email
from datetime import datetime

# Create your views here.

def root(request):
    return render(request, 'events/root.html')

def index(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = AddFriendForm()
            has_frequests = len(request.user.player.accepter.all())>0
            frequests = AcceptFriendForm(request.user)
            friends = request.user.player.friends.all()
            return render(request, 'events/index.html', {'form': form, 'friends': friends, 'frequests': frequests, 'has_frequests': has_frequests})
    return redirect('/')

def new_user(request):
    return render(request, 'events/signup.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.player.username = form.cleaned_data.get('username')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # django_rq.enqueue(welcome_email, user.email, user.player.activation)
            welcome_email(user.email, user.player.activation)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'events/signup.html', {'form': form})

def activate(request):
    # future - add resend activation email
    if 'q' in request.GET:
        if request.user.is_authenticated:
            code = request.GET['q']
            if request.user.player.activation == code:
                request.user.player.active = True
                request.user.is_active = True
                request.user.save()
                return render(request, 'events/active.html')
            else:
                return render(request, 'events/inactive.html')
        else:
            # future - do login redirect with q value
            render(request, 'events/inactive.html')
    return render(request, 'events/inactive.html')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'events/invalid_login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def create_event(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('/')
        form = UserEventForm(request.user)
        return render(request, 'events/create_event.html', {'form': form})
    elif request.method == 'POST':
        form = UserEventForm(request.user, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            occuring = datetime.combine(cd['event_date'], cd['event_time'])
            event = UserEvent(
                name = cd['name'],
            	description = cd['description'],
                location = cd['location'],
            	owner = request.user.player,
            	occuring = occuring,
            )
            event.save()
            event.member.add(*list(cd['attendees']))
            event.save()
            # django_rq.enqueue(new_event_email, event)
            new_event_email(event)

            return HttpResponse("working?")
        return HttpResponse('Invalid Form')

def friend_request(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AddFriendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                friend = Player.objects.get(username=cd['friend'])
                frequest = FriendRequest(requester=request.user.player, accepter=friend)
                frequest.save()
            except:
                try:
                    friend = User.objects.get(email=cd['efriend'])
                    frequest = FriendRequest(requester=request.user.player, accepter=friend.player)
                    frequest.save()
                except:
                    try:
                        frequest = NewMemberRequest(inviter=request.user.player, email=cd['efriend'])
                        # django_rq.enqueue(friend_invite_email, cd['efriend'])
                        friend_invite_email(cd['efriend'])
                    except:
                        message = "invalid username or email"
    return redirect('/events/')

def frequest(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AcceptFriendForm(request.user, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for friend_request in cd['requests']:
                request.user.player.friends.add(friend_request.requester)
            for friend_request in FriendRequest.objects.filter(accepter=request.user.player):
                friend_request.delete()
    return redirect('/events/')

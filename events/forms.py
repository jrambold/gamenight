from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from events.models import Player, UserEvent
from events.widgets import SelectTimeWidget


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=200, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserEventForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label='Location', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    event_date = forms.DateField(label='Date of the Event', widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ))
    event_time = forms.TimeField(label='Time of the Event', widget=SelectTimeWidget(twelve_hr=True, minute_step=5))
    attendees = forms.ModelMultipleChoiceField(label='Select Attendees', queryset=None, required=False, widget = forms.CheckboxSelectMultiple)
    invite_name = forms.CharField(label='Invite New User Name', max_length=200, required=False)
    invite_email = forms.EmailField(label='New User Email', max_length=254, help_text='Required. Enter a valid email address.', required=False)

    def __init__(self, user, *args, **kwargs):
        super(UserEventForm, self).__init__(*args, **kwargs)
        self.fields['attendees'].queryset = user.player.friends.all()

class AddFriendForm(forms.Form):
    friend = forms.CharField(label='Add Friend by Username', max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    efriend = forms.CharField(label='Add Friend by Email', max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class AcceptFriendForm(forms.Form):
    requests = forms.ModelMultipleChoiceField(label='Accept/Deny Friend Requests', queryset=None, required=False, widget = forms.CheckboxSelectMultiple)

    def __init__(self, user, *args, **kwargs):
        super(AcceptFriendForm, self).__init__(*args, **kwargs)
        self.fields['requests'].queryset = user.player.accepter.all()

class EventStatusForm(forms.Form):
    ATTENDING = 'Attending'
    MAYBE = 'Maybe'
    PASSING = 'Passing'
    AWAITING = 'Awaiting Response'
    STATUS_CHOICES = (
        (ATTENDING, 'Attending'),
        (MAYBE, 'Maybe'),
        (PASSING, 'Passing'),
        (AWAITING, 'Awaiting Response')
    )
    status = forms.ChoiceField(label='Change Status', choices=STATUS_CHOICES)

class GameForm(forms.Form):
    name = forms.CharField(label='Add Game', max_length=200)

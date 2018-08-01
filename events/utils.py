from django.core.mail import send_mail
from django.contrib.auth.models import User, Group
from events.models import Player, UserEvent

def welcome_email(email, code):
    send_mail('Welcome to Gamenight',
        f"""Activate your account.
        https://game-nighter.herokuapp.com/events/user/activate/?q={code}""",
        'gamemaster@game-nighter.herokuapp.com',
        [email],
        fail_silently=False)

def new_event_email(event):
    for member in event.member.all():
        send_mail('New Gamenight Invite!',
            f"""You have been invited to a new event!
            {event.name}
            Host: {event.owner.username}
            Date and Time: {event.occuring}
            Location: {event.location}

            {event.description}

            https://game-nighter.herokuapp.com/events/event/{event.id}/""",
            f"{event.owner.username}@game-nighter.herokuapp.com",
            [member.user.email],
            fail_silently=False)

def friend_invite_email(email):
    send_mail('A friend has invited you to Gamenight',
        f"""Click here to sign up.
        https://game-nighter.herokuapp.com/events/signup/""",
        'gamemaster@game-nighter.herokuapp.com',
        [email],
        fail_silently=False)

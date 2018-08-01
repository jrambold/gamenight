from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
import random


def random_string():
	return str(random.randint(10000, 99999))

# Create your models here.

class Player(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	username = models.CharField(max_length=200)
	friends = models.ManyToManyField("self")
	active = models.BooleanField(default=False)
	activation = models.CharField(max_length=200, default=random_string)

	def __str__(self):
		return self.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Player.objects.create(user=instance)
		instance.player.save()
		email = instance.email
		try:
			friends = NewMemberRequest.objects.filter(sender=email)
			for friend in friends:
				instance.player.friends.add(friend.requester)
				friend.delete()
		except:
			a = 'a'
	instance.player.save()

class FriendRequest(models.Model):
	requester = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='requester')
	accepter = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='accepter')

	def __str__(self):
		return f"{self.requester}"

class NewMemberRequest(models.Model):
	inviter = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='inviter')
	email = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.requester} wants to add {self.email}"

class Game(models.Model):
	name = models.CharField(max_length=200)

class UserEvent(models.Model):
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	description = models.TextField()
	owner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='owner')
	member = models.ManyToManyField(Player, related_name='member')
	occuring = models.DateTimeField(auto_now=False, auto_now_add=False)
	games = models.ManyToManyField(Game, related_name='userevent')

	def __str__(self):
		return self.name

class PlayerStatus(models.Model):
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
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AWAITING)
	event = models.ForeignKey(UserEvent, on_delete=models.CASCADE, related_name='memberstatus')
	player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='memberstatus')

	def __str__(self):
		return f"{self.event.name} {self.player.username}"

class InvitedUser(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=254)
	accepted = models.BooleanField(default=False)
	event = models.ForeignKey(UserEvent, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

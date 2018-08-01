from django.contrib import admin

# Register your models here.
from events.models import Player, UserEvent, FriendRequest, NewMemberRequest, PlayerStatus

admin.site.register(Player)
admin.site.register(UserEvent)
admin.site.register(FriendRequest)
admin.site.register(NewMemberRequest)
admin.site.register(PlayerStatus)

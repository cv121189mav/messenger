from django.contrib import admin
from.models import User, Notification, Activity, GroupChatting, PrivateChatting, Friendship
# Register your models here.

admin.site.register(User)
admin.site.register(Notification)
admin.site.register(Activity)
admin.site.register(GroupChatting)
admin.site.register(PrivateChatting)
admin.site.register(Friendship)

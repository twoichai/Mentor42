from django.contrib import admin

# Models are registered here

from .models import Room, Message, Topic, UserDetails

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(UserDetails)

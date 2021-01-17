from django.contrib import admin
from .models import Room,RoomRequest,RoomType

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(RoomRequest)
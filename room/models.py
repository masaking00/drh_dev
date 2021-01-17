import uuid

from django.db import models
from django.utils import timezone

class RoomType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    room_type_name = models.CharField(max_length=20,verbose_name="部屋タイプ名称")

    def __str__(self):
        return self.room_type_name

class Room(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    room_number = models.CharField(max_length=4,verbose_name="部屋番号")
    room_name = models.ForeignKey(RoomType,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.room_number

class RoomRequest(models.Model):
    choice_area =(
        (1,'タオル１組'),
        (2,'バスタオル'),
        (3,'フェイスタオル'),
        (4,'歯ブラシ'),
        (5,'貸出物'),
    )

    room_number = models.ForeignKey(Room,on_delete=models.CASCADE)
    request = models.IntegerField(choices=choice_area)
    request_time = models.DateTimeField(default=timezone.now)
    comp = models.BooleanField(default=False)

    def __str__(self):
        return str(self.room_number)
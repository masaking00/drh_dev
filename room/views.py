from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import RoomRequest

class TopView(generic.TemplateView):
    template_name = "room/top.html"

class ReservedView(generic.TemplateView):
    template_name = "room/reserved.html"

class RoomRequestListView(generic.ListView):
    model = RoomRequest

    template_name = 'room/roomrequest_list.html'

class RoomRequestCreateView(generic.CreateView):
    model = RoomRequest
    fields = ["room_number","request"]
    success_url = reverse_lazy('reserved')

class RoomRequestUpdateView(generic.UpdateView):
    template_name = 'room/roomrequest_update_form.html'
    model = RoomRequest
    fields = ["room_number","request","comp"]
    success_url = reverse_lazy('list')
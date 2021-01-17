from django.urls import path
from .views import RoomRequestListView,TopView,RoomRequestCreateView,ReservedView
from . import views

urlpatterns = [
    path('',views.TopView.as_view(),name="top"),
    path('roomrequest_list/',views.RoomRequestListView.as_view(),name="list"),
    path('roomrequest/',views.RoomRequestCreateView.as_view(),name="request"),
    path('<int:pk>/update/',views.RoomRequestUpdateView.as_view(),name="update"),
    path('reserved/',views.ReservedView.as_view(),name="reserved"),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='chat_room'),     # any string passed will be route to this path, this is going to create multiple chatrooms
]

from django.urls import path
from . import views

urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),
    # path('upload/', views.upload_file, name='upload_file'),
]

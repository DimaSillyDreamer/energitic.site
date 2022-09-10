
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.get_chat, name='get_chat')
]

from django.urls import path
from .views import SendMessage, ChatHistory

urlpatterns = [
    path('send-message/', SendMessage.as_view(), name='send-message'),
    path('chat-history/', ChatHistory.as_view(), name='chat-history'),
]

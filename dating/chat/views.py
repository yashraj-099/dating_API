from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Message

class SendMessage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Message.objects.create(
            sender=request.user,
            receiver_id=request.data['receiver_id'],
            message=request.data['message']
        )
        return Response({"message": "Sent"})


class ChatHistory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.GET.get('user_id')
        chats = Message.objects.filter(
            sender=request.user, receiver_id=user_id
        ) | Message.objects.filter(
            sender_id=user_id, receiver=request.user
        )

        return Response([
            {"msg": c.message, "time": c.created_at}
            for c in chats
        ])

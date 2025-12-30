from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

import math
from rest_framework.permissions import IsAuthenticated
from .models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"})
        return Response(serializer.errors, status=400)


import math
from rest_framework.permissions import IsAuthenticated
from .models import User

class NearbyUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
        users = User.objects.exclude(id=request.user.id)

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371
            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
            return R * 2 * math.asin(math.sqrt(a))

        result = []
        for user in users:
            distance = haversine(lat, lng, user.latitude, user.longitude)
            if distance <= 10:
                result.append({
                    "name": user.username,
                    "distance_km": round(distance, 2)
                })

        return Response(result)

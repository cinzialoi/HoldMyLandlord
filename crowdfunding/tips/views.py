from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tip
from django.contrib.auth import get_user_model
from .serializers import TipsSerializer
from django.http import Http404
from rest_framework import status

class TipJar(APIView):
    def get(self, request):
            tips = Tip.objects.all()
            serializer = TipsSerializer(tips, many=True)
            return Response(serializer.data)
    def post(self, request):
            serializer = TipsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(landlord = get_user_model().objects.order_by("?").first())
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                    )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

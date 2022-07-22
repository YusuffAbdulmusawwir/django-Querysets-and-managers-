from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from .models import Link
from links.serializers import LinkSerializer
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models 
from . import serializers

import datetime

# Create your views here.
class PostListApi(ListAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer
    queryset= Link.objects.all()

class PostCreateApi(CreateAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer


class PostDetailApi(RetrieveAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer
    queryset= Link.objects.all()

class PostUpdateApi(UpdateAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer


class PostDeleteApi(DestroyAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer

class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
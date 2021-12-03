from django.shortcuts import render

from .models import Wish, Gift
from rest_framework import viewsets
from .serializer import WishSerializer, GiftSrializer


class WishViewSet(viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSrializer

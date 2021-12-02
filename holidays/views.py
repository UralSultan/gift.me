from django.shortcuts import render

from .models import HolidayModel
from rest_framework import viewsets
from .serializers import HolidaySerializer


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = HolidayModel.objects.all()
    serializer_class = HolidaySerializer

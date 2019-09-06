from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from musica.models import Musica
from musica.serializers import MusicaSerializer


class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = MusicaSerializer

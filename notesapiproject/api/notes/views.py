# from django.shortcuts import render
from rest_framework import viewsets

# import local data
from .serializers import NoteSerializer
from .models import Note


# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def root(request):
    return JsonResponse({'text': 'you are in the api root'})

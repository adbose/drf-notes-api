from django.urls import path, include
# from rest_framework.authtoken import views
from .views import root


urlpatterns = [
    path('', root, name='api.root'),
    path('notes/', include('api.notes.urls')),
]
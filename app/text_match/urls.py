from django.urls import path

from .views import *


urlpatterns = [
    path('list-keys/', get_key, name="list-keys"),
    path('get-values/', get_values, name='get-values')
]

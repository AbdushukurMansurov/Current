from django.urls import path
from .views import index_function,chatgpt

urlpatterns = [
    path('', index_function, name='home'),
    path('chatgpt/', chatgpt, name='bot')
]
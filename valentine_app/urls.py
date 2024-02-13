from django.urls import path
from . import views

urlpatterns = [
    path('sender/', views.sender, name='sender'),
    path('receiver/<int:sender_id>/', views.receiver, name='receiver'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
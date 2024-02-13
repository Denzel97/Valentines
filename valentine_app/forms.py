from django import forms
from .models import Sender, Receiver

class SenderForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = ['sender_email']

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ['receiver_name', 'response']

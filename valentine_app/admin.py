from django.contrib import admin
from .models import Sender, Receiver

admin.site.register(Sender)
admin.site.register(Receiver)
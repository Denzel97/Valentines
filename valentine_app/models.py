import uuid
from django.db import models

class Sender(models.Model):
    sender_email = models.EmailField()
    unique_link = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def generate_unique_link(self):
        return f'receiver/{self.id}/'

class Receiver(models.Model):
    RESPONSE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    receiver_name = models.CharField(max_length=255)
    response = models.CharField(max_length=3, choices=RESPONSE_CHOICES)
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.receiver_name} - {self.response}"

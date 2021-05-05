from django.conf import settings
from django.db import models
from django.utils import timezone


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    sent_date = models.DateTimeField(blank=True, null=True)

    def send(self):
        self.sent_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

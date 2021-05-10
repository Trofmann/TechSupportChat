from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class ChatUser(models.Model):
    """Chat user class"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # type - manager or client
    type = models.CharField(max_length=7)


class Message(models.Model):
    """ Message class"""
    author = models.ManyToManyField(ChatUser, related_name="author")
    text = models.CharField(max_length=300)
    recipient = models.ManyToManyField(ChatUser, related_name="recipient")
    sent_date = models.DateTimeField(blank=True, null=True)

    def send(self):
        self.sent_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

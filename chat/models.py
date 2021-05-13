# coding=utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class ChatUser(models.Model):
    """Класс пользователя чата"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Тип - manager или client
    type = models.CharField(max_length=7)


class Message(models.Model):
    """ Класс сообщения """
    # Автор сообщения
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Текст соощения
    text = models.CharField(max_length=300)
    # Получатель сообщения
    # recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipient')
    # Дата отправки
    sent_date = models.DateTimeField()

    def send(self):
        self.sent_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

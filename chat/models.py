# coding=utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class ChatUser(models.Model):
    """Класс пользователя чата"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Тип - manager или client
    type = models.CharField(max_length=7)


class Message(models.Model):
    """ Класс сообщения """
    # Автор сообщения
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор сообщения')
    # Текст соощения
    text = models.CharField(max_length=300, verbose_name='Текст сообщения')
    # Получатель сообщения
    # recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipient')
    # Дата отправки
    sent_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
        ordering = ['sent_date']

    def __unicode__(self):
        return self.text

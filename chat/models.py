# coding=utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Пока не используется
class ChatUser(models.Model):
    """Класс пользователя чата"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Тип - manager или client
    type = models.CharField(max_length=7)


class Message(models.Model):
    """ Класс сообщения """
    # Автор сообщения
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор сообщения'
    )

    # Текст соощения
    text = models.CharField(
        max_length=300,
        verbose_name='Текст сообщения'
    )
    # Дата отправки
    sent_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата отправки'
    )

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
        ordering = ['sent_date']

    def __unicode__(self):
        return self.text


class Dialog(models.Model):
    """Класс диалога"""
    # Клиент - владелец диалога
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Клиент',
        related_name='client'
    )

    # Оператор, захвативший диалог
    operator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Опертор',
        related_name='operator',
        blank=True
    )
    # Сообщения, входящие в диалог
    messages = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name='Сообщение'
    )

    # Добавить метод передачи другому оператору

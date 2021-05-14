# coding=utf-8
from django import forms
from django.contrib.auth.models import User


class MessageForm(forms.Form):
    # Автор сообщения
    author = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    # Текст сообщения
    text = forms.CharField(max_length=300)
    # Получатель сообщения
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

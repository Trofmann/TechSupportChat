# coding=utf-8
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from .forms import MessageForm
from .models import Message


def message_list(request):
    # В случае POST-запроса обрабатываем данные
    if request.method == 'POST':
        # Создаем экземпляр формы и заполняем его данными из запроса
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            # Достаем из формы текст и автора сообщения
            new_message_text = message_form.cleaned_data['text']
            new_message_author = message_form.cleaned_data['author']
            # Создаем объект сообщения и сохраняем его
            new_message = Message(text=new_message_text, author=new_message_author)
            new_message.save()

    else:
        message_form = MessageForm()

    messages = Message.objects.all()
    return render(request, 'chat/message_list.html', {'messages': messages, 'form': message_form})

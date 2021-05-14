# coding=utf-8
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import MessageForm
from .models import Message


# Класс для создания сообщения
class MessageCreateView(CreateView):
    # Обработка GET-запроса
    def get(self, request, *args, **kwargs):
        context = {'form': MessageForm(), 'messages': Message.objects.all()}
        return render(request, 'chat/message_list.html', context)

    # Обработка POST-запроса
    def post(self, request, *args, **kwargs):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            # Достаем из формы текст и автора сообщения
            new_message_text = message_form.cleaned_data['text']
            new_message_author = message_form.cleaned_data['author']
            # Создаем объект сообщения и сохраняем его
            new_message = Message(text=new_message_text, author=new_message_author)
            new_message.save()
        context = {'form': MessageForm(), 'messages': Message.objects.all()}
        return render(request, 'chat/message_list.html', context)

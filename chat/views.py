# coding=utf-8
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from .forms import MessageForm
from .models import Message


def message_list(request):
    if request.method == 'POST':
        new_message_text = request.POST.get('text')
        new_message_author = User.objects.all()[int(request.POST.get('author'))]
        # Создаем объект сообщения
        new_message = Message(text=new_message_text, author=new_message_author)
        new_message.save()
        print(1)

    messages = Message.objects.all()
    message_form = MessageForm()
    return render(request, 'chat/message_list.html', {'messages': messages, 'form': message_form})

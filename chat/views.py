# coding=utf-8
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from .forms import MessageForm
from .models import Message


def message_list(request):
    if request.method == "POST":
        new_message_text = request.POST.get("text")
        print(new_message_text)
        # Создаем объект сообщения
        new_message = Message(text=new_message_text, author=User.objects.get(username='user'), sent_date=timezone.now())
        new_message.save()

    messages = Message.objects.all()
    message_form = MessageForm()
    return render(request, 'chat/message_list.html', {'messages': messages, 'form': message_form})

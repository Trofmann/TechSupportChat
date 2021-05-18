# coding=utf-8
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .forms import MessageForm
from .models import Message


# Класс для создания сообщения
class MessageCreateView(CreateView):
    # Обработка GET-запроса
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {'form': MessageForm(), 'messages': Message.objects.filter(author=request.user)}
            return render(request, 'chat/message_list.html', context)
        else:
            return redirect('login')

    # Обработка POST-запроса
    def post(self, request, *args, **kwargs):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.object = message_form.save(commit=False)
            message_form.object.author = request.user
            message_form.object.save()
        context = {'form': MessageForm(), 'messages': Message.objects.filter(author=request.user)}
        return render(request, 'chat/message_list.html', context)

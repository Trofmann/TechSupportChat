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
            # Достаем из формы текст и автора сообщения
            # new_message_text = message_form.cleaned_data['text']
            # new_message_author = message_form.cleaned_data['author']
            # # Создаем объект сообщения и сохраняем его
            # new_message = Message(text=new_message_text, author=new_message_author)
            message_form.object = message_form.save()
            message_form.object.author = request.user
            message_form.object.save()
            # new_message.save()
        context = {'form': MessageForm(), 'messages': Message.objects.filter(author=request.user)}
        return render(request, 'chat/message_list.html', context)

# class MessageCreateView(CreateView):
#     template_name = 'chat/message_list.html'
#     form_class = MessageForm
#
#     def form_valid(self, form):
#         self.object = form.save()
#         self.object.save()
#         context = {'form': MessageForm(), 'messages': Message.objects.all()}
#         return render('chat/message_list.html', context)

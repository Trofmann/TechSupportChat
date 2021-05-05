from django.shortcuts import render

from .models import Message


def message_list(request):
    messages = Message.objects.all()
    return render(request, 'chat/message_list.html', {'messages':messages})

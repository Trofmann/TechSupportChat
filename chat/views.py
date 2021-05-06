from django.shortcuts import render

from .forms import MessageForm
from .models import Message
from django.contrib.auth.models import User


def message_list(request):
    if request.method == "POST":
        new_message_text = request.POST.get("text")
        print(new_message_text)
        new_message = Message(text=new_message_text, author=User.objects.get(username='user'))
        new_message.send()

    messages = Message.objects.all()
    message_form = MessageForm()
    return render(request, 'chat/message_list.html', {'messages': messages, 'form': message_form})

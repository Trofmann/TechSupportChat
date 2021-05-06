from django.http import HttpResponse
from django.shortcuts import render

from .forms import MessageForm
from .models import Message


def message_list(request):
    if request.method == "POST":
        text = request.POST.get("text")
        #return HttpResponse("<h2>{0}</h2>".format(text))
        print(text)

    messages = Message.objects.all()
    message_form = MessageForm()
    return render(request, 'chat/message_list.html', {'messages': messages, 'form': message_form})

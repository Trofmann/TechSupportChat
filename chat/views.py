from django.shortcuts import render


def message_list(request):
    return render(request, 'chat/message_list.html', context={"letter": 123})

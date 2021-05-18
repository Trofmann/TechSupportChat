# coding=utf-8
from django import forms
from models import Message


# class MessageForm(forms.Form):
#     # Автор сообщения
#     author = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
#     # Текст сообщения
#     text = forms.CharField(max_length=300)
#     # Получатель сообщения
#     recipient = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # exclude = ()
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

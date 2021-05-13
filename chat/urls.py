from django.conf.urls import url

from .views import message_list

urlpatterns = [
    url(r'', message_list, name='message_list'),
]

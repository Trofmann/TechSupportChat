from django.conf.urls import url
from django.contrib.auth import views as auth_views

# from .views import message_list
#
# urlpatterns = [
#     url(r'', message_list, name='message_list'),
# ]

from .views import MessageCreateView

urlpatterns = [
    url(r'^messages', MessageCreateView.as_view(), name='message_list'),
    url(r'^', auth_views.login, {'template_name': 'chat/login.html'}, name='login')
]

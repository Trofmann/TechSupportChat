from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import MessageCreateView

urlpatterns = [
    url(r'^messages', login_required(MessageCreateView.as_view(), login_url='/chat/login'), name='message_list'),
    url(r'^', auth_views.login, {'template_name': 'chat/login.html'}, name='login')

]

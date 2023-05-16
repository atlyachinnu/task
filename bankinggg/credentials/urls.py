from django.urls import path

from credentials import views
from bankinggg import settings
from django.conf.urls.static import static

app_name = 'credentials'

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('new', views.new, name='new'),
    path('page', views.page, name='page'),
    path('message', views.message, name='message')



]

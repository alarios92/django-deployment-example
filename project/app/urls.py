from django.conf.urls import url
from app import views


app_name = "app"

urlpatterns=[
    url('register', views.register, name='register'),
    url('user_login',views.user_login, name='user_login'),
]

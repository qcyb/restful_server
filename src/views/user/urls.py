from django.urls import path
from views.user import views

user_urls = [
    path(r'', views.UserView.as_view()),
    path(r'/sync', views.UserSyncView.as_view()),
]

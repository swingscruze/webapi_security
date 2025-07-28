from django.urls import path
from . import views



urlpatterns = [


    path("", views.UserView.as_view()),
    path("home/", views.UserView.as_view()),
    path("adduser/", views.adduser),
    path("deleteuser/", views.deleteuser),
]



from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("live", views.live, name="live"),
    path("preview", views.preview, name="preview"),   
    path("logout/", views.logout_view, name="logout"),
]

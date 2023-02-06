from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('homepage', TemplateView.as_view(template_name='books/home.html'), name='home')
]
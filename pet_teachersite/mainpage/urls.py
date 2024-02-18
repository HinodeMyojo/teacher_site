from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', TemplateView.as_view(template_name='mainpage/main_page.html'),
         name='main_page'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('in_progress/', TemplateView.as_view(template_name='mainpage/in_progress.html'),
         name='in_progress')
]

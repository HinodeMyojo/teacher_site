from django.urls import path
from django.views.generic import TemplateView

app_name = 'mainpage'

urlpatterns = [
    path('', TemplateView.as_view(template_name='mainpage/main_page.html'),
         name='main_page'),
    path('sign_up/', TemplateView.as_view(template_name='mainpage/sign_up.html'),
         name='sign_up'),
    path('in_progress/', TemplateView.as_view(template_name='mainpage/in_progress.html'),
         name='in_progress')
]

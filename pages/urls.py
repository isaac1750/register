from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    
    path('fill', views.fill, name='fill'),
    path('thanks', views.thanks, name='thanks'),

  
    ]
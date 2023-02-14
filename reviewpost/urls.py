from django.urls import path
from . import views

urlpatterns = [
    #path('', views.hello)
    path('', views.signupview, name='signup'),
    path('login/', views.loginview, name='login'),
    #path('sample/', sampleview),
]

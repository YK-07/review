from django.urls import path
from . import views

urlpatterns = [
    #path('', views.hello)
    path('', views.signupview, name='signup'),
    path('login/', views.loginview, name='login'),
    path('list/', views.listview, name='list'),
    path('detail/<int:pk>/', views.detailview, name='detail'),
    path('create/', views.CreateClass.as_view(), name='create')
    #path('sample/', sampleview),
]
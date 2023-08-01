from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signin,name='signin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_event',views.add_event,name='add_event'),
    path('edit_event',views.edit_event,name='edit_event'),
    path('view_event',views.view_event,name='view_event'),
    path('forget_pass',views.forget_pass,name='forget_pass'),
]
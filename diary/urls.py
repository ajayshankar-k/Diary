from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signin,name='signin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_event',views.add_event,name='add_event'),
    path('edit_event/<int:id>',views.edit_event,name='edit_event'),
    path('view_event/<int:id>',views.view_event,name='view_event'),
    path('delete_event/<int:id>',views.delete_event,name='delete_event'),
    path('forget_pass',views.forget_pass,name='forget_pass'),
    path('signout',views.signout,name='signout'),
    path('change_pass',views.change_pass,name='change_pass')
]
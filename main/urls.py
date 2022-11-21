from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('create-post/', views.create_post, name='createpost'),
        
]

from django.contrib import admin
from django.urls import path
from . import views


from .views import  RegisterView,startapp,createview,startup_details,LoginView,CustomLogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('Register', RegisterView.as_view(), name='register'),
    #path('', views.startapp, name='startapp'),
    path('createview/', views.createview, name='createview'),
    path('update/<int:pk>/', views.update, name='update'),
    path('startup_details/<int:pk>/', views.startup_details, name='startup_details'),
    path('startup_delete/<int:pk>/', views.startup_delete, name='startup_delete'),
    path('startapp', views.startapp, name='startapp'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('startup_list/', views.startup_list, name='startup_list'),





]
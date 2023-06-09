from django.urls import path
from basic_app import views

# FOR TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('register', views.registration, name="registration"),
    path('user_login/', views.user_login, name="user_login")
]
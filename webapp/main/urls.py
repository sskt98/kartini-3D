from .views import user_login,user_logout
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path("photo/<int:pk>/", views.photo_detail, name="photo_detail"),
    path('contact/', views.contact, name='contact'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', views.signup, name='register'),
]

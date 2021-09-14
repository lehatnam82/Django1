from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('<str:slug>/', views.blog, name="blog"),
]

from . import views
from django.urls import path, include
from django.urls import reverse

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path("<int:id>/", views.post, name='post')
]
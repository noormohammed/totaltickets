from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('lots-of-things', views.index, name='index'),
]
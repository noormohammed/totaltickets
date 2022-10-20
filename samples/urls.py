from django.urls import path
from samples.views import SamplesView

urlpatterns = [
    path('', SamplesView.index, name='index'),
]
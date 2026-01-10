from django.urls import path
from .views import create_training, get_all_trainings, training_detail

urlpatterns = [
    path('', get_all_trainings),
    path('create/', create_training),
    path('<int:id>/', training_detail),
]

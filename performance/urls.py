from django.urls import path
from .views import (
    create_performance,
    get_all_performance,
    performance_detail
)

urlpatterns = [
    path('', get_all_performance),
    path('create/', create_performance),
    path('<int:id>/', performance_detail),
]

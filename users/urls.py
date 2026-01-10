from django.urls import path
from .views import create_user, get_all_users, user_detail

urlpatterns = [
    path('', get_all_users),
    path('create/', create_user),
    path('<int:id>/', user_detail),
]

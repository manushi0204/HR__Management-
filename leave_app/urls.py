from django.urls import path 
from .views import create_leave,get_all_leaves,leave_detail

urlpatterns = [
    path('', get_all_leaves), 
    path('create/', create_leave),    
    path('<int:id>/', leave_detail),
]

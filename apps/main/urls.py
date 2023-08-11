from django.urls import path
from .views import (
    list_todos, 
    create_tosos, 
    delete_todo,
    update_todo,
)


urlpatterns = [
    path('', list_todos),
    path('create/', create_tosos),
    path('delete/<int:pk>/', delete_todo),
    path('update/<int:pk>/', update_todo),
]
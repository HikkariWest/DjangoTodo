from django.urls import path, include
from django.views import *
from .views import *

urlpatterns = [
	path('', todo_list, name = 'todo_list'),
	path('<int:todo_id>/', todo_details, name = 'todo_details'),
	path('create_todo/', create_todo, name = 'create_todo'),
	path('<int:todo_id>/update_todo/', update_todo, name = 'update_todo'),
	path('<int:todo_id>/delete_todo/', delete_todo, name = 'delete_todo')
]

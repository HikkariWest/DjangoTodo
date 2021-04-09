from django.urls import path, include
from django.views import *
from .views import *

urlpatterns = [
	path('', todo_list, name = 'todo_list'),
	path('<uuid:todo_id>/', todo_details, name = 'todo_details'),
	path('create_todo/', create_todo, name = 'create_todo'),
	path('<uuid:todo_id>/update_todo/', update_todo, name = 'update_todo'),
	path('<uuid:todo_id>/delete_todo/', delete_todo, name = 'delete_todo')
]

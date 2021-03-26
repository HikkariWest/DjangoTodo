from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm
# Create your views here.

def todo_list(request):
	todos = TodoItem.objects.all()
	context = {'todos':todos}
	return render(request, 'todolist/todo_list.html', context)

def todo_details(request, todo_id):
	todo = TodoItem.objects.get(id = todo_id)
	context = {'todo':todo}
	return render(request, 'todolist/todo_details.html', context)

def searching_todo(request):
	if 'q' in request.GET:
		q = request.GET['q']
		todos2 = TodoItem.objects.filter(title__icontains = q)
	else:
		todos2 = TodoItem.objects.all()
	context = {'todos2': todos2}
	# return render(request, '', context)

def create_todo(request):
	form = TodoItemForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		return redirect('/todo/')

	context = {'form':form}
	return render(request, 'todolist/create_todo.html', context)


def update_todo(request, todo_id):
	todo = get_object_or_404(Post, id = todo_id)
	form = TodoItemForm(request.POST or None, instance = todo)
	if request.method == 'POST':
		form = TodoItemForm(request.POST, instance = todo)
		if form.is_valid():
			form.save()
			return redirect('/todo/'+todo_id)
	context = {'form':form}
	return render(request, 'todolist/update_todo.html', context)


def delete_todo(request, todo_id):
	todo = Post.objects.get(id = todo_id)
	if request.method == 'POST':
		todo.delete()
		return redirect('/todo/')
	context = {'todo':todo}
	return render(request, 'todolist/delete_todo.html', context)


# def todo_list(request):
# 	context = {}
# 	return render(request, 'todolist/...html', context)
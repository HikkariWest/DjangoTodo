from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def todo_list(request):
	search = request.GET.get('search','')
	if search:
		todos = TodoItem.objects.filter(
			Q(title__icontains = search)
				|
			Q(description__icontains = search))
		serialized_todo = serializers.serialize('json', todos, fields = ('title'))
		return JsonResponse({'todos':serialized_todo})
	else:
		todos = TodoItem.objects.all()
	context = {'todos':todos,
				'search':search}
	return render(request, 'todolist/todo_list.html', context)

def todo_details(request, todo_id):
	todo = TodoItem.objects.get(uu_id = todo_id)
	context = {'todo':todo}
	return render(request, 'todolist/todo_details.html', context)

def searching_todo(request):
	if 'search' in request.GET:
		q = request.GET['search']
		todos2 = TodoItem.objects.filter(title__icontains = search)
	else:
		todos2 = TodoItem.objects.all()
	# context = {'todos2': todos2}
	# return render(request, '', context)


def create_todo(request):
	form = TodoItemForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/todo/')
	context = {'form':form}
	return render(request, 'todolist/create_todo.html', context)


def update_todo(request, todo_id):
	todo = get_object_or_404(TodoItem, uu_id = todo_id)
	form = TodoItemForm(request.POST or None, instance = todo)
	if request.method == 'POST':
		form = TodoItemForm(request.POST, instance = todo)
		if form.is_valid():
			form.save()
			return redirect('/todo/'+uu_id)
	context = {'form':form}
	return render(request, 'todolist/update_todo.html', context)


def delete_todo(request, todo_id):
	todo = Post.objects.get(uu_id = todo_id)
	if request.method == 'POST':
		todo.delete()
		return redirect('/todo/')
	context = {'todo':todo}
	return render(request, 'todolist/delete_todo.html', context)


# def todo_list(request):
# 	context = {}
# 	return render(request, 'todolist/...html', context)
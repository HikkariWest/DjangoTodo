from django.contrib import admin
from .models import TodoItem, TestModel, Student
# Register your models here.
admin.site.register(TodoItem)
admin.site.register(TestModel)
admin.site.register(Student)
from django.contrib import admin
from .models import TodoItem, TestModel
# Register your models here.
admin.site.register(TodoItem)
admin.site.register(TestModel)
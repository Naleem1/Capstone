from django.views.generic import ListView   
from .models import ToDoItem, ToDoList 
from django.urls import reverse

class viewOfList(ListView):
    model = ToDoList
    template = 'main_app/index.html'

class ItemListView(ListView):
    model = ToDoItem
    template = 'main_app/todolist_list.html'

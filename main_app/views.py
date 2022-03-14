from django.views.generic import ListView   
from .models import ToDoItem, ToDoList 
from django.urls import reverse

class viewOfList(ListView):
    model = ToDoList
    template = 'main_app/index.html'

class ItemListView(ListView):
    model = ToDoItem
    template = 'main_app/todolist_list.html'

    def get_queryset(self):
        return ToDoItem.objects.filter(todolist_list_id = self.kwargs['list_id'])

    def get_context_data(self):
        context = super().get_context_data
        context['todolist_list'] = ToDoList.objects.get(id = self.kwargs['list_id'])
        return context
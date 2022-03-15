from pipes import Template
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.views.generic.base import TemplateView 
from .models import ToDoItem, ToDoList 
from django.urls import reverse


class ViewOfList(TemplateView):
    model = ToDoList
    template_name = 'main_app/index.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['todolist_list'] = ToDoList.objects.all()
        return context

class ItemListView(ListView):
    model = ToDoItem
    template = 'main_app/todolist_list.html'

    def get_queryset(self):
        return ToDoItem.objects.filter(todolist_list_id = self.kwargs['list_id'])

    def get_context_data(self):
        context = super().get_context_data
        context['todolist_list'] = ToDoList.objects.get(id = self.kwargs['list_id'])
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]
    success_url = "/"
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context
        
class ItemCreate(CreateView):
    model = ToDoItem
    fields = ['todo_list', 'title', 'description','due_date']

    def get_initial(self):
        initial_data = super(ItemCreate,self).get_initial()
        todo_list = ToDoList.objects.get( id = self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get( id = self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a New Item'
        return context 

    def get_success_url(self):
        return reverse('item_add', kwargs = {"id":self.id})
        
class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = ["todo_list","title","description","due_date", ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("item_update", kwargs={"id":self.id})
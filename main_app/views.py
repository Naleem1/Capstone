from django.views.generic import ListView   
from .models import ToDoList 

class viewOfList(ListView):
    model = ToDoList
    template = 'main_app/index.html'
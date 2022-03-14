from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.viewOfList.as_view(), name = "index")
]
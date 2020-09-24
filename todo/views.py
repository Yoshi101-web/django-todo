from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel

# Create your views here.

#()内は、継承
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
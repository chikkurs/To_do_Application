from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Todo
from .forms import Todoupdate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
import urllib
import urllib.request


# Create your views here.


def homepage(request):
    task1 = Todo.objects.all()
    if request.method == 'POST':
        task = request.POST['task']
        priority = request.POST['priority']
        date = request.POST['date']
        todo = Todo(task=task, priority=priority, date=date)
        todo.save()
    print('task created succesfully')
    return render(request, 'homepage.html', {'task1': task1})


def delete(request, taskid):
    task = Todo.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    todo = Todo.objects.get(id=id)
    todo1 = Todoupdate(request.POST or None, instance=todo)
    if todo1.is_valid():
        todo1.save()
        return redirect('/')
    return render(request, 'update.html', {'todo': todo, 'todo1': todo1})


class TodoListView(ListView):
    model = Todo
    template_name = 'homepage.html'
    context_object_name = 'task1'


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'plain.html'
    context_object_name = 'todo'


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'todo'
    fiels = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('homedetailview', kwargs={'pk': self.object.id})


class TodoDeleteView(DeleteView):
    mode = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('homelistview')

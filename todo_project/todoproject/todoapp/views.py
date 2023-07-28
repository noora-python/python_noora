from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import TodoForms
from todoapp.models import Task
from django.views.generic import ListView, DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView
# for listview

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'
class TaskDetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task'
# Create your views here.
class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url=reverse_lazy('TaskListView')

def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name1 =request.POST.get('task','')
        desc1 = request.POST.get('priority','')
        date = request.POST.get('date', '')
        todo=Task(name=name1,priority=desc1,date=date)
        todo.save()
        return redirect('/')


    return render(request,'home.html',{'task':task1})
def delete_task(request,taskid):
    task= Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render (request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    form1 =TodoForms (request.POST or None,instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'task': task,'forms':form1})
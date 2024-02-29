from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.

#class based Views

class TaskLiseView(ListView):
    model = Task
    template_name = 'cbvhome.html'
    context_object_name = 'task'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'cbvdetail.html'
    content_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'cbvupdate.html'
    content_object_name = 'task'
    fields = ('name', 'priority', 'date', 'desc')

    
    def get_success_url(self):
        return reverse_lazy ('cbvdetail', kwargs= {'pk': self.get_object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'cbvdelete.html'
    
    def get_success_url(self):
        return reverse_lazy ('cbvlist')


#function based views
def home(request):
    task=Task.objects.all()
    if request.method=='POST':
        #collect data from the input field
        name=request.POST.get('Task','')
        #collect data from the input field
        priority=request.POST.get('priority','')
        #collect data from the input field
        desc=request.POST.get('desc','')
        #collect data from the input filed
        date=request.POST.get('date', '')
        #saving datat to a veriable
        task1=Task(name=name,priority=priority,desc=desc, date=date)
        task1.save()
    return render(request, 'home.html',{'task': task})

def details(request):
    #saving datat to a veriable from database
    task=Task.objects.all()

    return render(request, 'details.html', {'task': task})


def delete (request, taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request, id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render (request, 'update.html',{'f':f, 'task':task})
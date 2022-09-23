from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from todo.models import Todo


# Create your views here
def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            tittle = request.POST['tittle']
        )
        new_todo.save()
        return redirect('/')
    
    return render(request,'todo/index.html',{'todos':todo})

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
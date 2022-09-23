from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo


# Create your views here
def index(request):
    todo = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    return render(request,'todo/index.html',{'todos':todo, 'form':form})

def deleteItem(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def updateItem(request,pk):
    update_todo = Todo.objects.get(id=pk)
    updateForm = TodoForm(instance = update_todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance = update_todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('/')
    return render(request,'todo/updateItem.html',{'update_todo':update_todo, 'updateForm':updateForm} )

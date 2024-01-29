from django.shortcuts import render,redirect
from . models import Task
from . forms import TodoForm
# Create your views here.

def index(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        age = request.POST.get('age','')
        place = request.POST.get('place','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        task = Task(name=name,age=age,place=place,email=email,phone=phone)
        task.save()
    return render(request, 'index.html',{'task1':task1})

def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')



def update(request,id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f':f,'task':task})






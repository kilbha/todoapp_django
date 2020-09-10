from django.shortcuts import render, redirect
from remapap.forms import todoform
from remapap.models import todo as td
# Create your views here.
def todo(request):
    form = todoform()
    tasks = td.objects
    if request.method == 'POST':
        form_instance = todoform(request.POST)
        form_instance.save()

    return render(request,'home.html',{'form':form,'tasks':tasks})

def deltask(request,prk):
    td.objects.filter(pk = prk).delete()
    return redirect('home')

def Edittask(request,prk):
    object = td.objects.filter(pk = prk).first()
    obj = td.objects.get(pk=prk)
    form = todoform(instance = object)
    if request.method == 'POST':
        form = todoform(request.POST)
        form_instance = form.save(commit=False)
        obj.task = form_instance.task
        obj.save()
        return redirect('home')
    return render(request,'edit.html',{'form':form})
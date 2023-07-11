from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.


def base(request):
    if(request.method == "POST"):
        data = request.POST
        task_name = data.get('task_name')

        todo.objects.create(
            task_name = task_name,
        )
        return redirect('/')
    queryset = todo.objects.all()
    context = {'base': queryset}
    return render(request,'index.html',context)

def delete_todo(request, id):
    queryset = todo.objects.get(id = id)
    queryset.delete()
    return redirect('/')
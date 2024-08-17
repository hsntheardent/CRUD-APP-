from multiprocessing import context
from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def Home(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        form=EmployeeForm()

    data=Employee.objects.all()




    context={
        'form':form,
        'data':data,
    }
    return render(request,'app1/index.html',context)


def Delete_record(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')

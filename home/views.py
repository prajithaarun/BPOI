from django.shortcuts import render, HttpResponse, redirect
from .models import student
from .form import studentform
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'index.html')


def insert(request):
    if request.method == 'GET':
        form = studentform()
        return render(request, 'insert.html', {'form': form})
    else:
        f = studentform(request.POST)
        if f.is_valid():
            f.save()
            f = studentform()
        return render(request, 'insert.html', {'form': f})

def display(request):
    object = student.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(object, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'pagination.html', { 'users': users})
# def display(request):
#     obj = student.objects.all()
#     # p = Paginator(obj, 4)
#     # obj= p.page(1)
#     return render(request, 'display.html', {'ob': obj})
#

'''obj=student.objects.get(id=5)
    return render(request, 'display1.html', {'ob': obj})
    obj = student.objects.filter(id=4)
    return render(request, 'display1.html', {'ob': obj})'''

def delete(request, id):
    ob = student.objects.get(id=id).delete()
    #return redirect('home:display')
    return HttpResponse("deleted sucessfully")


def update(request, pk):
    if request.method == 'GET':
        obj = student.objects.get(id=pk)
        return render(request, 'update.html', {'ob': obj})
    else:
        h = request.POST['name']
        p = request.POST['mark']
        s = request.POST['subject']
    student.objects.filter(id=pk).update(name=h, mark=p, subject=s)
    return redirect('home:display')

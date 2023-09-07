from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForms
from movieapp.models import Movies


# Create your views here.
def index(request):
    movie=Movies.objects.all() # for fetching all data
    context={'movie_list':movie}
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movies.objects.get(id=movie_id) # for getting only id
    return render(request,'detail.html',{'mov':movie})
def add_movie(request):
    if request.method=='POST':
        name1=request.POST.get('name')
        desc1 = request.POST.get('desc')
        year1 = request.POST.get('year')
        img1 = request.FILES['img']
        movie=Movies(name=name1,desc=desc1,year=year1,img=img1)
        movie.save()
        return redirect('/')

    return render(request,'add.html')
def update(request,id):
    mov=Movies.objects.get(id=id)
    form1 =MovieForms (request.POST or None,request.FILES,instance=mov)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'movies': mov,'forms':form1})
def delete(request,id):
    if request.method == 'POST':
        mov = Movies.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render (request,'edit.html')
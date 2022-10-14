from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request, 'index.html')

def form(request):
    if request.method == "post":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        fav_language = request.POST.get("fav_language")
        file = None
        if request.FILES:
            file = request.FILES['profile_pic']
            fs = FileSystemStorage()
            saved_file = fs.save(file.name,file)
            file_url = fs.url(saved_file)
        return HTTPResponse("<h1>FILE SUBMITTED {} <br> {} <br> {} <br> <img src='{}'></h1>".format(fname,lname,fav_language,file_url))



    return render(request, 'form.html')

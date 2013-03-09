from django.shortcuts import render_to_response
from student.models import Students
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def main_page(request):
    if request.method == 'GET':
        return render_to_response('main.html')
def details(request):
    if request.method == 'GET':
        return render_to_response('details.html',{})
    if request.method == 'POST':
        name =request.POST.get('studentname')
        sex =request.POST.get('sex')
        age =request.POST.get('age')
        mark =request.POST.get('mark')
        p = Students(name = name, sex = sex, age= age, mark= mark)
        p.save()
        return HttpResponse("""<html><div class=metanav>
                           <p><a href="/">Home</a></p>
			   </div><h2><center>!!.....Saved.....!!</h2></center></html>""")
def view(request):
    entries = Students.objects.all()
    return render_to_response('show.html', {'entries': entries})
def sort_age(request):
    entries = Students.objects.order_by('age')
    return render_to_response('show.html', {'entries': entries})
def sort_mark(request):
    entries = Students.objects.order_by('mark')
    return render_to_response('show.html', {'entries': entries})

def remove_details(request):
    if request.method == 'GET':
        return render_to_response('remove.html')
    if request.method == 'POST':
        name = request.POST.get('student_name')
        p = Students.objects.filter(name=name)
        p.delete()
        return HttpResponse("""<html><div class=metanav>
                           <p><a href="/">Home</a></p>
			   </div><body><h2><center>!....Removed....!</h2></center></body></html>""")
def search(request):
    if request.method == 'GET':
        return render_to_response('search.html')
    if request.method == 'POST':
        name = request.POST.get('student_name')
        entries = Students.objects.filter(name=name) 
        return render_to_response('show.html', {'entries': entries})

def login_details(request):
    
    if request.method == 'GET':
        return render_to_response("login.html")
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            
            return HttpResponseRedirect("/login_details/details/")
        else:
            return HttpResponse("Invalid username or password")    


def login_remove(request):
    
    if request.method == 'GET':
        return render_to_response("login.html")
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            
            return HttpResponseRedirect("/login_remove/remove/")
        else:
            return HttpResponse("Invalid username or password")

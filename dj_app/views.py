from django.shortcuts import render, redirect
from django.http import HttpResponse
from dj_app.models import *
import json
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def home_page(request):
    current_user = request.user.id
    print(current_user)
    response_data = {
        'h_content':'Home page dynamic content',
        'para_home':'A paragraph for the Home page',
        'home_anchor':'https://google.com'
    }
    return render(request, 'home.html', response_data)

def contact_us(request):
    client_info_data = [2,3,4,5]
    some_data_to_dump = {'client_data':200}
    data = json.dumps(some_data_to_dump)
    return HttpResponse(data, content_type='application/json')

def form_submission(request):
    if request.method == "GET":
        current_user = request.user.id
        print(current_user)
        return render(request, 'form.html')
    if request.method == "POST":
        user_file = request.FILES['u_image']
        client_info_data = client_info(
            client_name = request.POST.get("u_name"),
            client_age = request.POST.get("u_age"),
            client_city = request.POST.get("u_city"),
            client_food = request.POST.get("u_food"),
            client_phone = request.POST.get("u_phone"),
            client_image = user_file.name,
            client_id = request.user.id,
            )
        client_info_data.save()
        destination_folder = r"/Users/abhay/Documents/projects_batch3/Django/django_demo/dj_app/static/images/" + user_file.name
        with open(destination_folder, 'wb+') as destination_file:
            for chunk in user_file.chunks():
                destination_file.write(chunk)
        return render(request, 'form_success.html')
    
def users_list(request):
    all_user_data = client_info.objects.all().values()
    last_id = client_info.objects.latest('id')
    return render(request, 'users_list.html', {'users_list' : list(all_user_data) })

def profile(request, id):
    user_data = client_info.objects.filter(id = id).values()
    return render(request, 'profile.html', {'user_list' : list(user_data)})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("r_password")
        if password == repeat_password:
            user = User.objects.create_user(username = username, password = password)
            return redirect(home_page)
        else:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

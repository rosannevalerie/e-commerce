from django.shortcuts import render
from django.shortcuts import render, redirect
from main.forms import CandyEntryForm
from main.models import Candy
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    candy_entries = Candy.objects.filter(user=request.user)
    default_candies = [
        {'name': 'Gummy', 'price': 10000, 'description': 'Tuti fruity chewy candy', 'sweetness': 9},
        {'name': 'Chocolate', 'price': 15000, 'description': 'Dark chocolate with almond', 'sweetness': 9},
        {'name': 'Lollipop', 'price': 5000, 'description': 'Sweet and sour candy', 'sweetness': 9}
    ]

    new_candy = []
    for candy in candy_entries:
        new_candy.append({'name': candy.name, 'price': candy.price, 'description': candy.description, 'sweetness': candy.sweetness})
    all_candies = default_candies + new_candy
    
    context = {
        'candies': all_candies,
        'last_login': request.COOKIES['last_login'],
        'user_name': request.user.username
    }
    
    return render(request, "main.html", context)

def create_candy_entry(request):
    form = CandyEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        candy_entry = form.save(commit=False)
        candy_entry.user = request.user
        candy_entry.save()
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_candy_entry.html", context)

def show_xml(request):
    data = Candy.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Candy.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Candy.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Candy.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
from django.shortcuts import render
from django.shortcuts import render, redirect
from main.forms import CandyEntryForm
from main.models import Candy
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    candy_entries = Candy.objects.all()
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
        'candies': all_candies
    }
    
    return render(request, "main.html", context)

def create_candy_entry(request):
    form = CandyEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
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
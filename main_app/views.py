from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView

# Create your views here.
# are similar to controllers in express
# we will define functions here
# this function is called in the main_app/urls.py
def home(request):
    # could do dataabase logic here
    #and then
    # render take (request, template, data(optional))
    data = []
    return render(request, 'home.html', {'data': data})

def about(request):
    return render(request, 'about.html')    

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cat_details(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

# <%= cat.name %> ===    {{ cat.name}}
# <% if(cat.name === 'Billie' %>.... === {% if cat.name == 'Billie' %} 

class CatCreate(CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

def __str__(self):
    return self.name
    

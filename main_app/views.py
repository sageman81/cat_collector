from django.shortcuts import render, redirect
from .models import Cat, Toy # * imports everything
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import FeedingForm
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
    feeding_form = FeedingForm() # new instance of the form

    id_list = cat.toys.all().values_list('id')

    toys_cat_doesnt_have = Toy.objects.exclude(id__in=id_list)

    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form, # pass the form to the template
        'toys': toys_cat_doesnt_have
    })

def assoc_toy(request, pk, toy_id):
    Cat.objects.get(id=pk).toys.add(toy_id)
    return redirect('detail', cat_id=pk)
   
# <%= cat.name %> ===    {{ cat.name}}
# <% if(cat.name === 'Billie' %>.... === {% if cat.name == 'Billie' %} 

class CatCreate(CreateView):
    model = Cat # cat_form in templates
    fields = ['name', 'breed', 'description', 'age']

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

def add_feeding(request, cat_id):
    # request.POST === req.body
    # request.POST gets the data out of the form
    form = FeedingForm(request.POST)
    if(form.is_valid()):
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'
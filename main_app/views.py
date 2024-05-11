from django.shortcuts import render

cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Tom', 'breed': 'Tom', 'description': 'gentle and loving', 'age': 0},
]
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
    return render(request, 'cats/index.html', {'cats': cats})


# <%= cat.name %> ===    {{ cat.name}}
# <% if(cat.name === 'Billie' %>.... === {% if cat.name == 'Billie' %} 
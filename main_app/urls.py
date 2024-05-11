from django.urls import path
from . import views

# define urls in a urlpatterns list

urlpatterns = [
    # do not start urls with a /, its autmatic
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index' )
]


# later in templates we can reference that name for 
# navgations { url 'main_app.home' }
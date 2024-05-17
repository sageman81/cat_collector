from django.urls import path
from . import views

# define urls in a urlpatterns list

urlpatterns = [
    # do not start urls with a /, its autmatic
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index' ),
    path('cats/create/', views.CatCreate.as_view(), name= 'cats_create'),
    path('cats/<int:cat_id>/', views.cat_details, name='detail'), 
]


# later in templates we can reference that name for 
# navgations { url 'main_app.home' }
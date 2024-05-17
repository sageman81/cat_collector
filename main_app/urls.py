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
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'), 
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'), 
]


# later in templates we can reference that name for 
# navgations { url 'main_app.home' }
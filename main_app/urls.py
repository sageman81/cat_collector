from django.urls import path
from . import views

# define urls in a urlpatterns list

urlpatterns = [
    # do not start urls with /, it will be added automatically
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index' ),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create' ),
    path('cats/<int:cat_id>/', views.cat_details, name='detail'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('cats/<int:pk>/assoc_toy/<int:toy_id>', views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name="toys_detail"),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]

# later in templates we can reference that name for 
# navgations { url 'main_app.home' }

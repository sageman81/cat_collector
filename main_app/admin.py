# from django.contrib import admin
# from .models import Cat, Feeding
# # Register your models here.

# admin.site.register(Cat)
# admin.site.register(Feeding)

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)
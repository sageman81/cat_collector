from django.db import models
from django.urls import reverse
# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})
    
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    
    def __str__(self):
        return f"A cat named {self.name}, aged {self.age}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        'Cheat Meal',
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE) # related_name="feedings"

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
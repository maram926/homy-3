from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 




class ChefOffering(models.Model):
    CATEGORY_CHOICES = [
        ('savory', 'Savory'),
        ('sweet', 'Sweet'),
    ]

    name = models.CharField(max_length=255)  # e.g., "Gourmet Family Meals"
    description = models.TextField()  # Description of the offering
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price_range = models.CharField(max_length=50)  # e.g., "Affordable", "Premium"
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    chef_offering = models.ForeignKey(ChefOffering, related_name='dishes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # e.g., "Pasta Primavera"
    description = models.TextField()  # Description of the dish
    ingredients = models.TextField()  # e.g., "Tomatoes, Basil, Garlic, Olive Oil"
    price = models.DecimalField(max_digits=6, decimal_places=2)  # e.g., "12.99"
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True)

    def __str__(self):
        return self.name
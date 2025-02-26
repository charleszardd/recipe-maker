from django.db import models

class Recipe(models.Model):
    DIFFICULTY_LEVELS = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ]

    CATEGORIES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Snack', 'Snack')
    ]

    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_images', blank=True, null=True)
     
    category = models.CharField(max_length=100, choices = CATEGORIES)
    difficulty = models.CharField(max_length=100, choices = DIFFICULTY_LEVELS, default='Easy')

    calories = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    fats = models.IntegerField(blank=True, null=True)
    carbs = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

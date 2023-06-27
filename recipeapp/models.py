from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms


class Recipe(models.Model):
    """
    Model for generating Recipe Instances
    """
    # Array of available regions for 'region' field
    REGIONS = (
        ('Abruzzo', 'Abruzzo'),
        ('Aosta valley', 'Aosta valley'),
        ('Apulia', 'Apulia'),
        ('Basilicata', 'Basilicata'),
        ('Calabria', 'Calabria'),
        ('Campania', 'Campania'),
        ('Emilia-Romagna', 'Emilia-Romagna'),
        ('Friuli-Venezia Giulia', 'Friuli-Venezia Giulia'),
        ('Lazio', 'Lazio'),
        ('Liguria', 'Liguria'),
        ('Lombardy', 'Lombardy'),
        ('Marche', 'Marche'),
        ('Molise', 'Molise'),
        ('Piedmont', 'Piedmont'),
        ('Sardinia', 'Sardinia'),
        ('Sicily', 'Sicily'),
        ('Trentino-South Tyrol', 'Trentino-South Tyrol'),
        ('Tuscany', 'Tuscany'),
        ('Umbria', 'Umbria'),
        ('Veneto', 'Veneto'),
        ('Unknown', 'Region Unknown'),
        ('None', 'No Specific Region'),
    )
    
    # Recipe Fields
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)
    region = models.CharField(
        choices=REGIONS, max_length=80, default='None')
    city = models.CharField(max_length=80, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="my_recipe"
    )
    featured_image = CloudinaryField(
        'image', blank=True,
        default=(
            "https://res.cloudinary.com/dyoueyepq/"
            "image/upload/v1687522627/recipe-placeholder.jpg"
            )
        )
    excerpt = models.TextField(blank=True)
    prep_time = models.PositiveIntegerField()
    serves = models.CharField(max_length=80, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='recipe_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    # Function that returns name of the recipe
    def __str__(self):
        return self.name

    # Function to count the likes
    def number_of_likes(self):
        return self.likes.count()

    # Function that format Date of Created On
    def string_of_created_on(self):
        return self.created_on.strftime("%A %d %B %Y")

    def string_of_edited_on(self):
        return self.edited_on.strftime("%A %d %B %Y")


class Comment(models.Model):
    """
    Class extending modles.Model class.
    Generates a comment instance
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, unique=False)
    slug = models.SlugField(max_length=80, unique=True)
    region = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="my_recipe"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    prep_time = models.PositiveIntegerField()
    cooking_time = models.PositiveIntegerField()
    serves = models.PositiveIntegerField()
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
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

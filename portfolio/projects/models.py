from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.
class ProjectList (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), 
    MaxValueValidator(datetime.now().year)], help_text="Use the following format: <YYYY>")
    client = models.CharField(max_length=20)
    technologies = models.CharField(max_length=200)
    project_link = models.URLField (max_length=200)
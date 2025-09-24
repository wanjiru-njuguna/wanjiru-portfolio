from django.db import models

# Create your models here.
class ContactInfo (models.Model):
    title = models.CharField (max_length= 40)
    email = models.EmailField(max_length=200)
    upwork = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    linkedIn = models.URLField(max_length=200)

    def __str__(self):
        return self.title
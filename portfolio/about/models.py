from django.db import models

# Create your models here.
class About (models.Model):
    title = models.CharField(max_length=20)
    description= models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='about/')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
     return self.title
    
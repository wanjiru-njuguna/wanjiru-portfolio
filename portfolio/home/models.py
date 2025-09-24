from django.db import models

# Create your models here.
class HomePage(models.Model):
    title = models.CharField(max_length=400)
    bio = models.TextField()
    video = models.FileField(upload_to='home/',  blank=True, null=True)
    projects_link = models.URLField()

    def __str__(self):
     return self.title
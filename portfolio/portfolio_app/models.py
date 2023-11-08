from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    summary = models.TextField()
    skills = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.TextField()
    github_link = models.URLField(max_length=255)
    demo_link = models.URLField(max_length=255, blank=True)


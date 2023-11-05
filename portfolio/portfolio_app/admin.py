from django.contrib import admin

# Register your models here.
from portfolio_app.models import Resume, Project

admin.site.register(Resume)
admin.site.register(Project)

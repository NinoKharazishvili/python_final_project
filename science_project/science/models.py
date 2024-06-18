from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Scientist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="scientist/images")
    description = models.TextField(null=True, blank=True)
    url = models.URLField(blank=True)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']
    


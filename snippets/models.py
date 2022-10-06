from django.db import models


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()

    class Meta:
        ordering = ("created",)


class Snippet2(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.TextField()
    code = models.TextField()
    password = models.TextField()
    email = models.TextField()

    class Meta:
        ordering = ("created",)

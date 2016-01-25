from django.db import models

class Fiddle(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    context = models.TextField(null=True, blank=True)
    template = models.TextField(null=True, blank=True)
    styles = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

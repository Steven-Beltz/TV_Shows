from django.db import models

class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # show

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.CharField(max_length=255)
    network = models.ForeignKey(Network, related_name="show", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


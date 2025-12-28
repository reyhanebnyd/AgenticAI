from django.db import models


class Message(models.Model):
    text = models.TextField()
    status = models.CharField(max_length=20, null=True, blank=True, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    


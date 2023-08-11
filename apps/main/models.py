from django.db import models

class Todo(models.Model):
    done = models.BooleanField(default=False)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
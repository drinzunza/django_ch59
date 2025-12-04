from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="notes/", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
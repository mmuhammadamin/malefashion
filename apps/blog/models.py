from django.db import models
from django.contrib.auth.models import User
# Create your model


class Timestamp(models.Model):
    crated_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Tag(Timestamp):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Post(Timestamp):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='blog/',null=True)
    tags=models.ManyToManyField(Tag,blank=True)
    content=models.TextField()
    username=User.username


    def __str__(self):
        return self.title

class CommentModel(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()


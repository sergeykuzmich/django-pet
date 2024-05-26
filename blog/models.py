from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    tags = models.ManyToManyField("Tag")


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

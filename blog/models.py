from django.contrib.auth import get_user_model
from django.db import models

from utils.get_tags import get_tags


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    tags = models.ManyToManyField("Tag")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.tags.clear()
        tags = get_tags(self.content)
        for tag in tags:
            tag, _ = Tag.objects.get_or_create(name=tag)
            self.tags.add(tag)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

from django.contrib.auth import get_user_model
from django.db import models

from utils.get_tags import get_tags


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name="posts")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField("Tag", related_name="posts")
    views = models.PositiveIntegerField(default=0)

    @property
    def excerpt(self):
        return self.content[:150]

    def __str__(self):
        return self.title

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

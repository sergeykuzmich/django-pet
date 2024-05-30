from django.contrib import admin

from blog.models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "category", "views"]
    list_filter = ["author", "category"]

    fieldsets = [
        (
            None,
            {
                "fields": ["title", "category", "content", "author"],
            },
        )
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

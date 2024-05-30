from blog.models import Category, Tag


def all_categories(request):
    return {
        'all_categories': Category.objects.order_by('name').all(),
        'all_tags': Tag.objects.order_by('name').all(),
    }

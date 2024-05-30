from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from blog.forms import PostForm
from blog.models import Post, Category, Tag


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created_at').all()[:4]
        context['categories'] = Category.objects.annotate(posts_count=Count('posts')).order_by('-posts_count').all()[:5]
        context['tags'] = Tag.objects.annotate(posts_count=Count('posts')).order_by('-posts_count').all()[:15]
        return context


class PostListView(ListView):
    model = Post
    template_name = 'post/all.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class CategoryPostsListView(ListView):
    model = Post
    template_name = 'post/category-posts.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(id=self.kwargs['pk']).first()
        return context

    def get_queryset(self):
        return Category.objects.get(pk=self.kwargs['pk']).posts.order_by('-created_at')


class TagPostsListView(ListView):
    model = Post
    template_name = 'post/tag-posts.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.filter(id=self.kwargs['pk']).first()
        return context

    def get_queryset(self):
        return Tag.objects.get(pk=self.kwargs['pk']).posts.order_by('-created_at')


class PostView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        post.views += 1
        post.save()
        return post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/create.html'

    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/edit.html'

    def test_func(self):
        return self.get_object().author_id == self.request.user.id

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.id})


class AnalyticsView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'analytics.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_views = Post.objects.order_by('-views')[:10]
        author_views = User.objects.annotate(total_post_views=Sum('posts__views'), total_posts=Count('posts')).order_by(
            '-total_post_views')[:7]
        context['post_views'] = post_views
        context['author_views'] = author_views
        return context

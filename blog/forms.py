from django.forms import ModelForm, ModelChoiceField, TextInput, Textarea, Select

from blog.models import Post, Category


class PostForm(ModelForm):
    category = ModelChoiceField(queryset=Category.objects.all(), required=True, widget=Select(attrs={
        'class': 'block w-full h-8 rounded-md border-0 py-1.5 pl-2 pr-4 text-gray-900 shadow-sm outline-0 text-sm '
                 'leading-6'}))

    class Meta:
        model = Post
        fields = ['category', 'title', 'content']

        widgets = {
            'title': TextInput(attrs={
                'class': 'block flex-1 border-0 bg-transparent py-1.5 px-3 text-gray-900 placeholder:text-gray-400 '
                         'focus:ring-0 text-sm leading-6 outline-0'}),
            'content': Textarea(attrs={
                'class': 'block w-full rounded-md outline-0 border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 '
                         'ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset '
                         'focus:ring-indigo-600 text-sm leading-6', 'rows': 5}),
        }

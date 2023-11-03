from django import forms
from .models import Blog
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'article_image']


from django import forms

from .models import BlogPost


class BlogForm(forms.ModelForm):
    """新建表格界面"""
    class Meta:
        model = BlogPost
        fields = ['title']
        labels = {'title': ''}


from django import forms
from .models import *


class ArticleCreateForm(forms.ModelForm):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Article
        fields = {'title', 'body', 'category', 'image', 'tags', 'status'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input--style-5'}),
            'body': forms.Textarea(attrs={'class': 'input--style-5', 'col': 40, 'row': 20}),
            'status': forms.TextInput(attrs={'class': 'input--style-5'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name', 'email', 'body'}

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

class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm mr-3 w-75 my-5',
               'placeholder':'Search'}))

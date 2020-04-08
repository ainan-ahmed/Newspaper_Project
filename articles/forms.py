from django import forms
from .models import Category,Article

class ArticleCreateForm(forms.ModelForm):
    category  = forms.ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model = Article
        fields = {'title','body','category','image'}
        
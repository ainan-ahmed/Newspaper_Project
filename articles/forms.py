from django import forms
from .models import Category,Article

class ArticleCreateForm(forms.ModelForm):
    category  = forms.ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model = Article
        fields = {'title','body','category','image'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'input--style-5'}),
            'body':forms.Textarea(attrs={'class':'input--style-5','col':40,'row':20})
        }
        
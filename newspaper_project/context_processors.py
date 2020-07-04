from articles.models import Category
from taggit.models import Tag
def add_variable_to_context(request):
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all()
    }
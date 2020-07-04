from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Article


class LatestArticlesFeed(Feed):
    title = 'News24'
    link = reverse_lazy('articles:list')
    description = "New articles from News24"

    def items(self):
        return Article.published_article.all()[:5]

    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return truncatewords(item.body,30)

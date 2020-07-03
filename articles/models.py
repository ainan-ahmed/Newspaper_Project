from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid
import readtime
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from .managers import PublishedManager
# Create your models here.


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TaggableManager(through=UUIDTaggedItem)
    image = models.ImageField(upload_to='images/', blank=True)
    views = models.IntegerField(default=0)
    objects = models.Manager()
    published_article = PublishedManager()
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub(self):
        return self.published.strftime('%b %e %Y')

    def year(self):
        return self.published.strftime('%Y')

    def month(self):
        return self.published.strftime('%b')

    def day(self):
        return self.published.strftime('%d')

    def countWords(self):
        return readtime.of_text(self.body)

    def get_absolute_url(self):
        return reverse('article:details', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'

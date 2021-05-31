from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author',verbose_name=_("author"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=100)
    tags = TaggableManager(_("tags"))
    image = models.ImageField(_("image"), upload_to='post/')
    created_at = models.DateTimeField(_("created at"), default=timezone.now)
    description = models.TextField(_("description"), max_length=15000)
    category = models.ForeignKey('Category', related_name='post_category',verbose_name=_("category"), on_delete=models.CASCADE)
    slug = models.SlugField(_('url'),blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(_('slug'), blank=True, null=True)

    def __str__(self):
        return self.name

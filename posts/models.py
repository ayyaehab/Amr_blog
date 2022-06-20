from django.db import models

# Create your models here.
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):
    postSlug = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    overview = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='static/imgs/posts', default=True)
    smalltitle = models.CharField(max_length=80)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.postSlug)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

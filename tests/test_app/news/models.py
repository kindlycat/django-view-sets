from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField('Title', max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['title', 'pk']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Title', max_length=100)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['title', 'pk']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField('Title', max_length=100)
    body = models.TextField('Body')
    publish_date = models.DateTimeField('Publish date', default=timezone.now)
    is_public = models.BooleanField('Is public', default=False)

    category = models.ForeignKey(
        to=Category,
        verbose_name='Category',
        related_name='news',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(
        to=Tag,
        verbose_name='Tags',
        related_name='news',
        blank=True
    )

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        ordering = ['title', 'pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/'


class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    file_obj = models.ImageField('Image', upload_to='news')
    description = models.CharField('Description', max_length=300, blank=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
        ordering = ['position', 'pk']

    def __str__(self):
        return self.file_obj.name

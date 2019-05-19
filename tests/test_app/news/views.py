from django.forms import inlineformset_factory
from django.urls import path
from django.utils.safestring import mark_safe

from tests.test_app.news.models import News, NewsImage
from viewsets import ModelViewSet, ViewSetDetailView, ViewSetSerializer


class PreviewView(ViewSetDetailView):
    template_name = 'staff/news/preview.html'
    model = News


class NewsMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        if 'cat_pk' in self.kwargs:
            return qs.filter(category=self.kwargs.get('cat_pk'))
        return qs


class NewsSerializer(ViewSetSerializer):
    def get_preview_value(self, obj):
        preview = obj.images.first()
        if preview:
            return mark_safe(
                '<a href="{0}" target="_blank"><img src="{0}" class="img-thumbnail" '
                'style="max-width:150px; max-height:150px"></a>'.format(preview.file_obj.url)
            )


class NewsViewSet(ModelViewSet):
    list_fields = ('title', 'preview', 'category', 'publish_date', 'is_public')
    detail_fields = ('title', 'body', 'publish_date', 'is_public', 'tags')
    fields = ('title', 'body', 'category', 'tags', 'publish_date', 'is_public')
    lookups = ('category',)
    autocomplete = ('tags',)
    search_fields = ('title',)
    filterset_fields = ('is_public', 'category', 'tags')
    default_value = '—'
    filterset_autocomplete = ('tags',)
    filterset_lookups = ('category',)
    serializer = NewsSerializer

    base_mixin = NewsMixin

    formset_classes = [
        inlineformset_factory(
            News,
            NewsImage,
            fields=('file_obj', 'description'),
            extra=0,
            can_order=True
        )
    ]

    def get_urls(self):
        return super().get_urls() + [
            path('<slug:pk>/preview/', self.get_view(PreviewView, 'preview'), name='preview')
        ]


class CategoryViewSet(ModelViewSet):
    available_views = ['list', 'create', 'update', 'delete']

    def get_urls(self):
        return super().get_urls() + [
            path('<slug:cat_pk>/news/', NewsViewSet.as_crud(model=News, viewset=self.viewset))
        ]

from django.forms import inlineformset_factory
from django.utils.safestring import mark_safe

from tests.test_app.test_models.models import (
    InlineModel, InlineModel2, TestModel
)
from viewsets import ModelViewSet, ViewSetSerializer


class CustomListSerializer(ViewSetSerializer):
    def get_dynamic_field_value(self, obj):
        return self.get_obj_link(obj, 'pk = {}'.format(obj.pk))

    def handle_image_file(self, obj, field, value):
        if value:
            return mark_safe(
                '<a href="{0}" target="_blank"><img src="{0}" class="img-thumbnail" '
                'style="max-width:150px; max-height:150px"></a>'.format(value.url)
            )


class TestMixin:
    def get_initial(self):
        if self.action == 'create':
            return {'char_field': 'initial_value'}
        return {}


class TestModelViewset(ModelViewSet):
    list_fields = ('char_field', 'image_field', 'fk_field', 'checkbox_field', 'dynamic_field')
    list_fields_names = {'fk_field': 'OtherModel', 'dynamic_field': 'Dynamic'}
    detail_fields = ('char_field', 'checkbox_field', 'inlines')
    detail_fields_names = {'char_field': 'title'}
    search_fields = ('char_field',)
    filterset_fields = ('checkbox_field', 'fk_field')
    filterset_order_by = ('char_field', ('dynamic_field', 'id'), 'checkbox_field')
    serializer = CustomListSerializer
    autocomplete = ('fk_field', 'other',)
    lookups = ('fk_field',)
    formset_autocomplete = {'inlines2': ('other',)}
    filterset_lookups = ('fk_field',)

    base_mixin = TestMixin
    formset_classes = [
        inlineformset_factory(
            TestModel,
            InlineModel,
            fields=('char_field', 'checkbox_field'),
            extra=0,
            can_order=True
        ),
        inlineformset_factory(
            TestModel,
            InlineModel2,
            fields=('char_field', 'checkbox_field', 'other'),
            extra=0,
            can_order=False,
        )
    ]

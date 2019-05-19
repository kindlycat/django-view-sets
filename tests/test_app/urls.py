from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from tests.test_app.news.models import Category, News, Tag
from tests.test_app.news.views import CategoryViewSet, NewsViewSet
from tests.test_app.test_models.models import OtherModel, TestModel
from tests.test_app.test_models.views import TestModelViewset
from viewsets import ViewSet, ViewSetIndexView


staff_viewset = ViewSet('staff', view_index=ViewSetIndexView)
admin_viewset = ViewSet('admin', view_index=ViewSetIndexView)


admin_viewset.register(Group, available_view=['list', 'create', 'update', 'delete'])
admin_viewset.register(
    User,
    fields=('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser'),
    list_fields=('username', 'is_staff'),
    detail_fields=('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
)

staff_viewset.register(TestModel, TestModelViewset)
staff_viewset.register(
    OtherModel, autocomplete_search_fields=('char_field',), search_fields=('char_field',)
)

staff_viewset.register(News, NewsViewSet)
staff_viewset.register(Category, CategoryViewSet)
staff_viewset.register(
    Tag,
    autocomplete_search_fields=('title',),
    available_views=['list', 'create', 'update', 'delete']
)


urlpatterns = [
    path('', LoginView.as_view(template_name='index.html', redirect_authenticated_user=True)),
    path('logout/', LogoutView.as_view(next_page='/')),
    path('staff/', staff_viewset.urls),
    path('admin/', admin_viewset.urls),
    path('news/', NewsViewSet.as_crud(model=News)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

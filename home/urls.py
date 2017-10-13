from django.conf.urls import url
from django.views.generic import DetailView
from django.conf import settings
from .models import Post
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home_list, name='home_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
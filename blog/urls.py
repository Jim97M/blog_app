from django import contrib
from django.contrib import admin, sitemaps
from django.urls import path, include
from myblog.sitemap import PostSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'posts':PostSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myblog.urls")),
    path(
        'sitemap.xml',sitemap, {'sitemaps':sitemaps}, name='django.contrib.views.sitemap')
]

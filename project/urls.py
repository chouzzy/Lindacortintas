from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import StaticViewSitemap, SnippetSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'snippet': SnippetSitemap
}

urlpatterns = [
    path('',include('app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('admin/', admin.site.urls),
]

handler404 = 'app.views.handler404'
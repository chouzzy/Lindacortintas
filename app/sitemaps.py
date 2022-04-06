from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Snipped

class StaticViewSitemap(Sitemap):
   changefreq= 'monthly'
   priority = 1

   def items(self):
      return ['index'] #colocar nada caso precise
      
   def location(self, item):
      return reverse(item)

class SnippetSitemap(Sitemap):

   def items(self):
      return Snipped.objects.all()
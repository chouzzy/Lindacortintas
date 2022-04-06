from django.db import models
from django.utils.text import slugify


#você escreveu snipped, mas era snippet. Na hora de abrir o manage.py as shell, muda isso se precisar: troca por snippet
# Snipped.objects.create(title ='H1 Snipped', body='<h1></h1>').save()
# Snipped.objects.create(title ='H2 Snipped', body='<h2></h2>').save()

class Snipped(models.Model): 
   title = models.CharField(max_length=150)
   slug = models.SlugField(blank=True, null=True)
   body = models.TextField()

   def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)

   def get_absolute_url(self):
      return f'/{self.slug}/'
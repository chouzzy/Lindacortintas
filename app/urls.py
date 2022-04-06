from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
   path('<slug:slug>/', views.snippet_detail),
   path('', views.index, name = 'index'),
   # path('second_page', views.second_page, name = 'second_page'),
]
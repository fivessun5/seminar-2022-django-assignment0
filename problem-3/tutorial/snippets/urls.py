from django import urls
from rest_framework import urlpatterns as patterns
from snippets import views

urlpatterns = [
    urls.path("snippets/", views.snippet_list),
    urls.path("snippets/<int:pk>/", views.snippet_detail),
]

urlpatterns = patterns.format_suffix_patterns(urlpatterns)
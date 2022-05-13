"""Django Config APP MDA Urls"""

# Libraries
from django.urls import path, include


urlpatterns = [
    path("sustentacionclases/", include("sustentacionclase.urls")),
]
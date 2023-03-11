from django.contrib import admin
from django.urls import path

from sahan.clips.views import clip, index

urlpatterns = [
    path("", index),
    path("CanItın/", admin.site.urls),  # noqa: RUF001
    path("<str:ident>/", clip, name="clip"),
]

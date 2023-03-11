import mimetypes
import random

from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache

from sahan.clips.models import Clip


@never_cache
def index(request):
    clips = Clip.objects.filter(is_active=True).values_list("ident", flat=True)
    if not clips:
        return HttpResponse("<h1>418 I'm a Teapot</h1>", status=418)

    ident = random.choice(clips)
    return redirect(reverse("clip", kwargs={"ident": ident}))


def clip(request, ident):
    try:
        obj = Clip.objects.get(is_active=True, ident__iexact=ident)
    except Clip.DoesNotExist:
        raise Http404

    real, given = obj.ident, ident
    if given != real:
        return redirect(reverse("clip", kwargs={"ident": real}))

    name, path = obj.file.name, obj.file.url
    mimetype, _ = mimetypes.guess_type(name)
    mimetype = mimetype or "text/plain"

    headers = {
        "X-Accel-Redirect": path,
        "Content-Type": mimetype,
    }
    return HttpResponse(headers=headers)

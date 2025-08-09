from django.shortcuts import render
from django.conf import settings
from django.utils._os import safe_join
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

entries =util.list_entries()

def page(request, page):
    if page in entries:
        finalPage = util.get_entry(page)
        return HttpResponse(finalPage)
    else:
        notfound = util.get_entry("NotFound")
        return HttpResponse(notfound)



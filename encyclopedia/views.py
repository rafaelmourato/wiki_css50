from django.shortcuts import render, redirect
from django.conf import settings
from django.utils._os import safe_join
from django.http import HttpResponse
from . import util

entries =util.list_entries()

def index(request):
    if request.method == "GET" and request.GET.get("q") != None and request.GET.get("q") != '':
        search = request.GET.get("q")
        if search in entries:
            return redirect('page', page=search)
        else:
            matched_entries = [entry for entry in entries if search.lower() in entry.lower()]
            return render(request, "encyclopedia/search.html", {
            "entries": matched_entries,
            "search": search
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def page(request, page):
    if page in entries:
        finalPage = util.get_entry(page)
        return HttpResponse(finalPage)
    else:
        notfound = util.get_entry("NotFound")
        return HttpResponse(notfound)



from django.shortcuts import render, redirect
from django.conf import settings
from django.utils._os import safe_join
from django.http import HttpResponse
from . import util
import random

entries = util.list_entries() 
search_entries = [low.lower() for low in util.list_entries()]

def index(request):
    if request.method == "GET" and request.GET.get("q") != None and request.GET.get("q") != '':
        search = request.GET.get("q")
        if search.lower() in search_entries:
            return redirect('page', page=search)
        else:
            matched_entries = []
            for entry in entries:
                if search.lower() in entry.lower():
                    matched_entries.append(entry)
            return render(request, "encyclopedia/search.html", {
            "entries": matched_entries,
            "search": search
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def page(request, page):
    if page.lower() in search_entries:
        finalPage = util.get_entry(page)
        return HttpResponse(finalPage)
    else:
        return render(request, "encyclopedia/notfound.html")

def newPage(request):
    return render(request, "encyclopedia/newpage.html")

def randomPage(request):
    max = len(entries)
    random_int = random.randint(0, max - 1)
    print(random_int)
    random_page = entries[random_int]
    return HttpResponse(util.get_entry(random_page))

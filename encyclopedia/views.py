from django.shortcuts import render, redirect
from django.conf import settings
from django.utils._os import safe_join
from django.http import HttpResponse
from django import forms
from . import util
import markdown2
import random

entries = util.list_entries() 
search_entries = [low.lower() for low in util.list_entries()]

class PageForm(forms.Form):
    title =  forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea)


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
        content = markdown2.markdown(finalPage)
        return render(request, "encyclopedia/page.html", {
            "title": page,
            "content": content
        })
    else:
        return render(request, "encyclopedia/notfound.html")

def newPage(request): 
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title not in entries:
                util.save_entry(title,content)
                return HttpResponse(util.get_entry(title))           
            else:
                return render(request, "encyclopedia/newpage.html",{
                "form": PageForm(request.POST),
                "error": "Title already in use"
                })    
    return render(request, "encyclopedia/newpage.html",{
        "form": PageForm()
    })

def randomPage(request):
    max = len(entries)
    random_int = random.randint(0, max - 1)
    print(random_int)
    random_page = entries[random_int]
    return HttpResponse(util.get_entry(random_page))

def editPage(request,title):
    if request.method == "POST":
        form = PageForm(request.POST)
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        util.save_entry(title,content)
        return HttpResponse(util.get_entry(title))
    else:
        page = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html", {
            "form": PageForm(initial={
            "title": title,
            "content": page
        })
        })
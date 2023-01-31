from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

posts = [
    {
        "author": "Chris",
        "title": "First post",
        "content": "some content here",
        "date_posted": "27 Aug 2022",
    },
    {
        "author": "Ez",
        "title": "second post",
        "content": "some more content here",
        "date_posted": "29 Aug 2022",
    },
]


def home(request: HttpRequest) -> HttpResponse:
    context = {"posts": posts}
    return render(request, "blog/home.html", context=context)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/about.html", {"title": "About"})

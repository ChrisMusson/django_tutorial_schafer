from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>This is the BLOG home</h1>")


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Blog ABOUT</h1>")

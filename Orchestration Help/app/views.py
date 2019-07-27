"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/index.html",
        {
            "title":"Home Page",
            "year":datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/contact.html",
        {
            "title":"Contact",
            "message":"Contact me via e-mail:",
            "year":datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/about.html",
        {
            "title":"About",
            "message":"This website records my experience of orchestration, which maybe helpful to anyone looking up for information on the topic.",
            "year":datetime.now().year,
        }
    )

def instruments(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/instruments.html",
        {
            "title":"Instruments",
            "message":"A summary page of different instruments.",
            "year":datetime.now().year,
        }
    )

def specific_instrument(request, instrument):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "instruments/" + instrument + ".html",
        {
            "year":datetime.now().year,
        }
    )
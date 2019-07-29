"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages

from .forms import SearchInstrumentForm as SIF

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/index.html",
        {
            "title": "Home Page",
            "year": datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/contact.html",
        {
            "title": "Contact",
            "message": "Contact me via e-mail:",
            "year": datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "app/about.html",
        {
            "title": "About",
            "message": "This website records my experience of orchestration, which maybe helpful to anyone looking up for information on the topic.",
            "year": datetime.now().year,
        }
    )

def instruments(request):

    assert isinstance(request, HttpRequest)

    if request.method == "GET":
        form = SIF(request.GET)
        if form.is_valid():
            instrument = form.cleaned_data
            a = instrument["search_instrument"].lower()
            if a == "":
                None
            elif a == "flute" or a == "oboe" or a == "clarinet" or a == "bassoon" or a == "saxophone" or a == "horn" or a == "trumpet" or a == "trombone" or a == "tuba" or a == "timpani" or a == "cymbal" or a == "violin" or a == "viola" or a == "violoncello" or a == "contrabass":
                return HttpResponseRedirect(a + "/")
            elif a == "sax" or a == "soprano sax" or a == "soprano saxophone" or a == "alto sax" or a == "alto saxophone" or a == "tenor sax" or a == "tenor saxophone" or a == "baritone sax" or a == "baritone saxophone":
                return HttpResponseRedirect("saxophone/")
            elif a == "french horn":
                return HttpResponseRedirect("horn/")
            elif a == "alto trombone" or a == "tenor trombone" or a == "bass trombone":
                return HttpResponseRedirect("trombone/")
            elif a == "bass drum":
                return HttpResponseRedirect("bass_drum/")
            elif a == "snare" or a == "snare drum":
                return HttpResponseRedirect("snare_drum/")
            elif a == "cello":
                return HttpResponseRedirect("violoncello/")
            elif a == "bass" or a == "double bass":
                return HttpResponseRedirect("contrabass/")
            else:
                messages.add_message(request, messages.INFO, "Sorry, your input is invalid, or the instrument hasn't been added yet.")
        else:
            form = SIF()

    return render(
        request,
        "app/instruments.html",
        {
            "title": "Instruments",
            "message": "A summary page of different instruments.",
            "year": datetime.now().year,
            "form": form,
        }
    )

def specific_instrument(request, instrument):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        "instruments/" + instrument + ".html",
        {
            "year": datetime.now().year,
        }
    )
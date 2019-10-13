"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class SearchInstrumentForm(forms.Form):
    search_instrument = forms.CharField(label = "", max_length = 100, required = False)
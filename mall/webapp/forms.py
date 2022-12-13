from django import forms
from django.forms import widgets
from webapp.models import Stufs, Stufs_in_cart
from django.core.validators import BaseValidator, ValidationError
from django.utils.deconstruct import deconstructible

class StufsForm(forms.ModelForm):
    class Meta:
        model = Stufs
        fields = ['stuf', 'description', 'categories', 'remainder', 'price']
        # exclude = []

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')

class StufsCartForm(forms.ModelForm):
      class Meta:
          model = Stufs_in_cart
          fields = ['stuf_key', 'amount_stuf']


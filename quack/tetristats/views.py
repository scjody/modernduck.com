from django.shortcuts import render
from django.views.generic.base import TemplateView

home = TemplateView.as_view(template_name='tetristats/home.html')

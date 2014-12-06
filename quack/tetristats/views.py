from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from tetristats.models import Stat, StatForm


home = TemplateView.as_view(template_name='tetristats/home.html')


@csrf_exempt
def collector(request):
    form = StatForm(request.POST)
    form.save()

    return HttpResponse(status=201)


def show(request):
    stats = Stat.objects.all()
    return render(request, 'tetristats/stats.html', {'stats': stats})

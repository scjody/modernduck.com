import datetime

from django.db.models import Avg, Max, Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from tetristats.models import Stat, StatForm


home = TemplateView.as_view(template_name='tetristats/home.html')


@csrf_exempt
def collector(request):
    uuid = request.POST.get('uuid')
    old_stat = None
    if uuid:
        try:
            old_stat = Stat.objects.get(uuid=uuid)
        except Stat.DoesNotExist:
            pass

    if old_stat:
        form = StatForm(request.POST, instance=old_stat)
    else:
        form = StatForm(request.POST)

    form.save()

    return HttpResponse(status=201)


def show(request):
    show_start = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)
    stats = Stat.objects.filter(timestamp__gte=show_start)
    if stats.count() < 5:
         stats = Stat.objects.all().order_by('-timestamp')[0:5]

    agg = Stat.objects.all().aggregate(
        Avg('total_gas'),
        Avg('time'),
        Sum('total_gas'),
        Sum('time'),
        Max('total_gas'),
        Max('score'),
        Max('lines'),
        Max('time'),
    )

    agg['gas_rate__avg'] = agg['total_gas__sum'] / agg['time__sum']

    context = {
        'stats': stats,
        'agg': agg,
    }

    return render(request, 'tetristats/stats.html', context)

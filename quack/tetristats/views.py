import datetime

import plotly.plotly as py
import plotly.graph_objs as pyg

from django.db.models import Avg, Count, Max, Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from tetristats.models import Stat, StatForm


py.sign_in("JodyMcintyre", "htzkacen0d")
home = TemplateView.as_view(template_name='tetristats/home.html')
faq = TemplateView.as_view(template_name='tetristats/faq.html')


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


def stats(request):
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
        Count('time'),
    )

    agg['gas_rate__avg'] = agg['total_gas__sum'] / agg['time__sum']

    update_plotly_graph()

    context = {
        'stats': stats,
        'agg': agg,
        'pagename': 'stats',
    }

    return render(request, 'tetristats/stats.html', context)


def update_plotly_graph():
    allstats = Stat.objects.all()
    times = [s.time for s in allstats]
    total_gas_consumptions = [s.total_gas for s in allstats]

    trace1 = pyg.Scatter(
        x=times,
        y=total_gas_consumptions,
        mode='markers',
        marker=pyg.Marker(
            color='rgb(255, 100, 0)',
            size=12,
            line=pyg.Line(
                color='white',
                width=0.5
            ),
        ),
    )
    data = pyg.Data([trace1])
    layout = pyg.Layout(
        title='Gas Consumption vs. Play Time',
        xaxis=pyg.XAxis(
            title='Play Time (seconds)',
        ),
        yaxis=pyg.YAxis(
            title='Gas Consumption (cats)',
        ),
    )
    figure = pyg.Figure(data=data, layout=layout)
    py.plot(figure, filename='Gas Consumption vs. Play Time', auto_open=False)

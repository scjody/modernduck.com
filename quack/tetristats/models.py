from django.db import models
from django.forms import ModelForm


class Stat(models.Model):
    uuid = models.CharField(max_length=36)
    total_gas = models.FloatField()
    score = models.IntegerField()
    lines = models.IntegerField()
    time = models.IntegerField()
    complete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)


class StatForm(ModelForm):
    class Meta:
        model = Stat
        exclude = ['timestamp']

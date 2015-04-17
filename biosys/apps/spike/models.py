from __future__ import unicode_literals
from django.db import models
from openpyxl import Workbook


class MyModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,
                            verbose_name="The verbose name.",
                            help_text="The help text")


def export_template(model):
    meta = model._meta
    wb = Workbook()
    ws1 = wb.active
    ws1.title = meta.model_name
    names = [f.name for f in meta.fields]
    ws1.append(names)

    wb.save(filename='template.xlsx')
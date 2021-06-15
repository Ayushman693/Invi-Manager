# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from docs_management import models

admin.site.register(models.UploadedDoc)
admin.site.register(models.ExtractedDoc)
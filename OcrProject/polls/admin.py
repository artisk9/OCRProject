# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Register your models here.
from django.contrib import admin
from OcrProject.polls.models import Document

admin.site.register(Document)

from django.shortcuts import render
from django.contrib.auth.models import Use
FIELDNAME = JSONField()


def profile(request):
    return
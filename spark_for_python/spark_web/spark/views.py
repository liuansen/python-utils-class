# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage
from django.views.decorators.csrf import  csrf_exempt

from run_spark import SparkWeb


spark = None


def login(request):
    app_name = request.GET.get('app_name')
    global spark
    spark = SparkWeb(app_name)
    return JsonResponse({'status': True})


def execute(request):
    print spark

    return JsonResponse({'status': True})



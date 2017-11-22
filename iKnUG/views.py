# -*- coding: utf-8 -*-
from django.template import loader, RequestContext
from django.shortcuts import render_to_response

def context_proc(request):
    return {
        'title': 'iKnUG',
        'appname': 'iKnUG'
    }

def home(request):
    return render_to_response(
        'index.html',
        context = RequestContext(request, processors = [context_proc])
    )

def icons(request):
    return render_to_response(
        'icons.html',
        context = RequestContext(request, processors=[context_proc])
    )

def charts(request):
    return render_to_response(
        'charts.html',
        context = RequestContext(request, processors=[context_proc])
    )

def forms(request):
    return render_to_response(
        'forms.html',
        context = RequestContext(request, processors=[context_proc])
    )

def login(request):
    return render_to_response('login.html')

def panels(request):
    return render_to_response(
        'panels.html',
        context = RequestContext(request, processors=[context_proc])
    )

def tables(request):
    return render_to_response(
        'tables.html',
        context = RequestContext(request, processors=[context_proc])
    )

def widgets(request):
    return render_to_response(
        'widgets.html',
        context = RequestContext(request, processors=[context_proc])
    )
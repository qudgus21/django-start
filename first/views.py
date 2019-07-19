from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from datetime import datetime

import random


def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)
    # <p>{{ current_date | date: "Y년 m월 d일 H시 i분 s초" }}</p>


def select(request):
    template = loader.get_template('first/select.html')
    context = {}
    return HttpResponse(template.render(context, request))


def result(request):
    chosen = int(request.GET['number'])
    results = []
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)
    box = []
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers': results
    }
    print(results)
    return render(request, 'first/result.html', context)

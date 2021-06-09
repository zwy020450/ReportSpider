import operator

from django.http import HttpResponse
from django.shortcuts import render
from Model.models import Report
import json

def show(request):
    data_list = Report.objects.all()
    data = []
    for var in data_list:
        row = {'title': var.title,
               'reporter': var.reporter,
               'notice_time': var.notice_time,
               'report_time': var.report_time,
               'address': var.address,
               'link': '<a href="'+var.link+'" target="_blank">点击前往</a>',
               'university': var.university
               }
        data.append(row)
    data.sort(key=operator.itemgetter('report_time'), reverse=True)
    return render(request, 'index.html', locals())


def get(request):
    return render(request, 'test.html')


def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def schoolfilter(request):
    school=request.GET.get('school')
    print(school)
    data_list = Report.objects.filter(university=school)
    data = []
    for var in data_list:
        row = {'title': var.title,
               'reporter': var.reporter,
               'notice_time': var.notice_time,
               'report_time': var.report_time,
               'address': var.address,
               'link': '<a href="'+var.link+'" target="_blank">点击前往</a>',
               'university': var.university
               }
        data.append(row)
    data.sort(key=operator.itemgetter('report_time'), reverse=True)
    return render(request, 'index.html', locals())
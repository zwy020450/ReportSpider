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
    if len(school)>0:
        print(school)
        data_list = Report.objects.filter(university=school)
    else:
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

def sort(request):
    sort=request.GET.get('sort')
    print( sort)
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
    if sort=='r1':
        data.sort(key=operator.itemgetter('report_time'), reverse=False)
    elif sort=='r0':
        data.sort(key=operator.itemgetter('report_time'), reverse=True)
    elif sort=='n1':
        data.sort(key=operator.itemgetter('notice_time'), reverse=False)
    else:
        data.sort(key=operator.itemgetter('notice_time'), reverse=True)
    return render(request, 'index.html', locals())

def timefilter(request):
    time=request.GET.get('time')
    print(time)
    data_list = Report.objects.all()
    data = []
    for var in data_list:
        if var.notice_time[:7]!=time :
            continue
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
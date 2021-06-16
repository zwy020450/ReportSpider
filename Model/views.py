import operator
from django.http import HttpResponse
from django.shortcuts import render
from Model.models import Report,CodeReport
import json
current_db=Report

def show(request):
    data_list = current_db.objects.all()
    data = []
    for var in data_list:
        row = {'title': var.title,
               'reporter': var.reporter,
               'notice_time': var.notice_time,
               'report_time': var.report_time,
               'address': var.address,
               'link': '<a href="'+var.link+'" target="_blank ">点击前往</a>',
               'university': var.university
               }
        data.append(row)
    data.sort(key=operator.itemgetter('notice_time'), reverse=False)
    return render(request, 'index.html', locals())

def schoolfilter(request):
    school=request.GET.get('school')
    if len(school)>0:
        print(school)
        data_list = current_db.objects.filter(university=school)
    else:
        data_list = current_db.objects.all()
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
    data_list = current_db.objects.all()
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
    data_list = current_db.objects.all()
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

def Codeshow(request):
    data_list = CodeReport.objects.all()
    data = []
    for var in data_list:
        row = {'title': var.title,
               'reporter': var.reporter,
               'notice_time': var.notice_time,
               'report_time': var.report_time,
               'address': var.address,
               'link': '<a href="'+var.link+'" target="_blank ">点击前往</a>',
               'university': var.university
               }
        data.append(row)
    data.sort(key=operator.itemgetter('report_time'), reverse=True)
    return render(request, 'index_code.html', locals())

def Codeschoolfilter(request):
    school=request.GET.get('school')
    if len(school)>0:
        print(school)
        data_list =CodeReport.objects.filter(university=school)
    else:
        data_list = CodeReport.objects.all()
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
    return render(request, 'index_code.html', locals())

def Codesort(request):
    sort=request.GET.get('sort')
    print( sort)
    data_list = CodeReport.objects.all()
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
    return render(request, 'index_code.html', locals())

def Codetimefilter(request):
    time=request.GET.get('time')
    print(time)
    data_list =CodeReport.objects.all()
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
    return render(request, 'index_code.html', locals())

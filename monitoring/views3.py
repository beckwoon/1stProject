from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import *
from monitoring.models import Data
from remgt.models import ReManagement
from django.db.models import Count, Sum
from datetime import datetime

@login_required

def ban_board(request):
    a = datetime.now().year
    year = int(request.GET.get("year",a))
    b = datetime.now().month
    month = int(request.GET.get("month", b))

    fc2019 = [531, 454, 558, 544, 660, 620, 553, 524, 558, 597, 776, 482]
    fc2020 = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

    counts = []
    count = {}
    j = 0
    if year == 2019:
        for i in fc2019:
            j += 1
            k = 'f'+str(j)
            count[k] = i
        for i in range(1, 13):
            c = Data.objects.filter(a_rdate__year=year, a_rdate__month=i).aggregate(Count('id'))
            k = 'm'+str(i)
            try:
                e = ReManagement.objects.filter(car_date__year=year, car_date__monte=i).aggregate(Count('id'))
                count[k] = c['id__count'] - e['id__count']
            except:
                count[k] = c['id__count']


    if year == 2020:
        for i in fc2020:
            j += 1
            k = 'f' + str(j)
            count[k] = i
        for i in range(1, 13):
            c = Data.objects.filter(a_rdate__year=year, a_rdate__month=i).aggregate(Count('id'))
            k = 'm' + str(i)
            try:
                e = ReManagement.objects.filter(car_date__year=year, car_date__monte=i).aggregate(Count('id'))
                count[k] = c['id__count'] - e['id__count']
            except:
                count[k] = c['id__count']

    count['year'] = year
    count['month'] = month
    try:
        monthcm = ReManagement.objects.filter(car_date__year=year, car_date__monte=month).aggregate(Count('id'))
        monthcn = Data.objects.filter(a_rdate__year=year, a_rdate__month=month).aggregate(Count('id'))
        count['monthc'] = monthcn['id__count'] - monthcm['id__count']

        yearcm = ReManagement.objects.filter(car_date__year=year).aggregate(Count('id'))
        yearcn = Data.objects.filter(a_rdate__year=year).aggregate(Count('id'))
        count['yearc'] = yearcn['id__count'] - yearcm['id__count']
    except:
        monthcn = Data.objects.filter(a_rdate__year=year, a_rdate__month=month).aggregate(Count('id'))
        count['monthc'] = monthcn['id__count']

        yearcn = Data.objects.filter(a_rdate__year=year).aggregate(Count('id'))
        count['yearc'] = yearcn['id__count']
    count['time'] = datetime.now()
    counts.append(count)

    d = {}
    dds = []
    if year == 2019:
        if month == 1:
            j = 0
            ds = 30
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                d[m] = '-'
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(Count('id'))
                d[m] = dc['id__count']

        if month == 2:
            j = 0
            ds = 27
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month-1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 29
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 3:
            j = 0
            ds = 24
            for i in range(ds, 29):
                j += 1
                k = 'd' + str(j)
                m = 'c'+ str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 4:
            j = 0
            ds = 31
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 31
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 5:
            j = 0
            ds = 28
            for i in range(ds, 31):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 6:
            j = 0
            ds = 26
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 31
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 7:
            j = 0
            ds = 30
            for i in range(ds, 31):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 8:
            j = 0
            ds = 28
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 9:
            j = 0

            de = 31
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 10:
            j = 0
            ds = 29
            for i in range(ds, 31):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 11:
            j = 0
            ds = 27
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 31
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 12:
            j = 0

            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

    if year == 2020:
        if month == 1:
            j = 0
            ds = 29
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=2019, a_rdate__month=12, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 2:
            j = 0
            ds = 26
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 30
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 3:
            j = 0

            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 4:
            j = 0
            ds = 29
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 31
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 5:
            j = 0
            ds = 26
            for i in range(ds, 31):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 6:
            j = 0
            ds = 31
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 31
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 7:
            j = 0
            ds = 28
            for i in range(ds, 31):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 8:
            j = 0
            ds = 26
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 9:
            j = 0
            ds = 30
            for i in range(ds, 32):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 31
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 10:
            j = 0
            ds = 27
            for i in range(ds, 31):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 11:
            j = 0
            de = 31
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']

        if month == 12:
            j = 0
            ds = 29
            for i in range(ds, 31):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month - 1, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
            de = 32
            for i in range(1, de):
                j += 1
                k = 'd' + str(j)
                m = 'c' + str(j)
                d[k] = i
                dc = Data.objects.filter(a_rdate__year=year, a_rdate__month=month, a_rdate__day=i).aggregate(
                    Count('id'))
                d[m] = dc['id__count']
    d['year'] = year
    d['month'] = month
    dds.append(d)


    return render(request, 'monitoring/ban_board.html', {'counts':counts, 'dds':dds})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from monitoring.models import *
from django.db.models import Count, Sum
from datetime import datetime

@login_required

def re_board(request, mn):
    counts=[]
    count = {}

    a = datetime.now().year
    b = request.GET.get("year",a)
    if mn == 0:
        c = Recovery.objects.filter(rq_ex=1, car_date__year=b).aggregate(Count('rq_ex'))
        d = Recovery.objects.filter(price_ex=1, car_date__year=b).aggregate(Count('price_ex'))
        dd = Recovery.objects.filter(price_ex=1, car_date__year=b).aggregate(Sum('rq_price'))
    else:
        c = Recovery.objects.filter(rq_ex=1, car_date__year=b, car_date__month=mn).aggregate(Count('rq_ex'))
        d = Recovery.objects.filter(price_ex=1, car_date__year=b, car_date__month=mn).aggregate(Count('price_ex'))
        dd = Recovery.objects.filter(price_ex=1, car_date__year=b, car_date__month=mn).aggregate(Sum('rq_price'))
    e = Recovery.objects.filter(outstanding1=1, car_date__year=b).aggregate(Count('outstanding1'))
    f = Recovery.objects.filter(outstanding2=1, car_date__year=b).aggregate(Count('outstanding2'))
    ff = Recovery.objects.filter(outstanding2=1, car_date__year=b).aggregate(Sum('rq_price'))
    count['year'] = b
    i = 1
    for i in range(1,13):
        g = Recovery.objects.filter(rq_ex=1, car_date__year=b, car_date__month=i).aggregate(Count('rq_ex'))
        h = Recovery.objects.filter(price_ex=1, car_date__year=b, car_date__month=i).aggregate(Count('price_ex'))
        k = 'm' + str(i)
        l = 'n' + str(i)
        count[k] = g['rq_ex__count']
        count[l] = h['price_ex__count']

    count['rq_ex'] = c['rq_ex__count']
    count['price_ex'] = d['price_ex__count']
    count['price1'] = dd['rq_price__sum']
    try:
        count['avg'] = int(dd['rq_price__sum'] / d['price_ex__count'])
    except:
        count['avg'] = None
    count['out1'] = e['outstanding1__count']
    count['out2'] = f['outstanding2__count']
    count['price2'] = ff['rq_price__sum']
    count['price3'] = 0
    count['price4'] = 0

    lists = []
    list = {}

    outs = Recovery.objects.filter(outstanding1=1, car_date__year=b)
    for out in outs:
        try:
            list['id'] = out.id
            list['car_num'] = out.car_num
            list['car_date'] = out.car_date
            list['model'] = out.car_model
            list['rq_ex'] = out.rq_ex
            list['num'] = out.rp_num
            list['car_data'] = out.car_data_id
            lists.append(list)
            list = {}
        except:
            None

    outss = Recovery.objects.filter(outstanding2=1, car_date__year=b)
    for out in outss:
        try:
            list['id'] = out.id
            list['car_num'] = out.car_num
            list['car_date'] = out.car_date
            list['model'] = out.car_model
            list['price_ex'] = out.price_ex
            list['price'] = out.rq_price
            try:
                RM = RecoveryMgt.objects.get(R_data_id=list['id'])
                if RM.receive1 is None: RM.receive1 = 0
                if RM.receive2 is None: RM.receive2 = 0
                if RM.receive3 is None: RM.receive3 = 0
                list['in_price'] = RM.receive1 + RM.receive2 + RM.receive3
                list['miss'] = list['price'] - list['in_price']
            except:
                list['in_price'] = 0
                list['miss'] = list['price'] - list['in_price']
            list['car_data'] = out.car_data_id
            count['price3'] += list['miss']
            lists.append(list)
            list = {}
        except:
            None
    outsss = Recovery.objects.filter(prog=1, car_date__year=b)
    for out in outsss:
        try:
            list['id'] = out.id
            list['car_num'] = out.car_num
            list['car_date'] = out.car_date
            list['model'] = out.car_model
            list['prog'] = out.prog
            list['price'] = out.rq_price
            try:
                RM = RecoveryMgt.objects.get(R_data_id=list['id'])
                if RM.receive1 is None: RM.receive1 = 0
                if RM.receive2 is None: RM.receive2 = 0
                if RM.receive3 is None: RM.receive3 = 0
                list['in_price'] = RM.receive1 + RM.receive2 + RM.receive3
                list['miss'] = list['price'] - list['in_price']
            except:
                list['in_price'] = 0
                list['miss'] = list['price'] - list['in_price']
            list['car_data'] = out.car_data_id
            count['price4'] += list['miss']
            lists.append(list)
            list = {}
        except:
            None

    counts.append(count)
    lists = sorted(lists, key=lambda x:x['id'], reverse=True)

    return render(request, 'recovery/re_board.html', {'counts':counts, 'lists':lists, 'mn':mn})

def recovery_create(request, pk):

    data = Data.objects.get(id=pk)

    if request.method == 'POST':
        a = request.POST["aa"]
        b = request.POST["bb"]
        c = request.POST["cc"]
        d = request.POST["dd"]
        e = request.POST["ee"]
        h = request.POST["hh"]
        l = request.POST["ll"]
        m = request.POST["mm"]
        n = request.POST["nn"]

        car_num = data.car_num2
        car_date = data.a_rdate
        car_model = data.car_type
        appraiser = a
        ap_grade = b

        if c == "":
            re_num = 0
        else:
            re_num = c

        if d == "":
            rp_num = 0
            rq_ex = False
            out1 = False
        else:
            rp_num = d
            rq_ex = True
            out1 = True

        re_part = e

        if h == "":
            rq_number = None
        else:
            rq_number = h
            out1 = False

        if l =="":
            rq_price = 0
            price_ex = False
            out2 = False
            prog = False
        else:
            rq_price = l
            price_ex = True
            out2 = True
            prog = False

        cus_number = m
        text = n.replace("/r/n","<br>")

        save_data = Recovery(
            car_data = data,
            car_num = car_num,
            car_date = car_date,
            car_model = car_model,
            appraiser = appraiser,
            ap_grade = ap_grade,
            rq_ex = rq_ex,
            price_ex=price_ex,
            outstanding1 = out1,
            outstanding2 = out2,
            prog = prog,
            re_num = re_num,
            rp_num =rp_num,
            re_part = re_part,
            rq_number = rq_number,
            rq_price = rq_price,
            cus_number = cus_number,
            text = text
        )
        save_data.save()

        m_data = Data.objects.get(id=pk)
        m_data.ex = True
        m_data.save()

        return redirect('/recovery/0')

    return render(request,'recovery/re_create.html', {'data':data})


from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class RecoveryUpdatelView(UpdateView):
    model = Recovery
    fields = ['appraiser', 'ap_grade', 're_part', 'rq_ex', 're_num', 'rp_num', 'rq_number', 'outstanding1',  'price_ex', 'rq_price', 'outstanding2', 'prog', 'cus_number', 'text']
    success_url = "/recovery/0"
    template_name = 'recovery/re_update.html'


def recovery_delete(request, pk):
    rdata = Recovery.objects.get(id=pk)
    pk2 = int(rdata.car_data_id)
    data = Data.objects.get(id=pk2)

    rdata.delete()
    data.ex = False
    data.save()

    return redirect('/recovery/0')

def recovery_detail(request, pk):
    data = Recovery.objects.get(car_data_id=pk)
    pk2 = data.id
    data3 = {}
    try:
        data2 = RecoveryMgt.objects.get(R_data_id=pk2)

        if data2.receive1:
            data3['total'] = data2.receive1
            data3['miss'] = data.rq_price - data3['total']

        if data2.receive2:
            data3['total'] += data2.receive2
            data3['miss'] = data.rq_price - data3['total']
        if data2.receive3:
            data3['total'] += data2.receive3
            data3['miss'] = data.rq_price - data3['total']

    except:
        data2 = None
        data3['miss'] = data.rq_price

    return render(request, 'recovery/re_detail.html', {'data':data, 'data2':data2, 'data3':data3})

def mgt_detail(request, pk):
    try:
        data = RecoveryMgt.objects.get(R_data_id=pk)
        data3 = {}
        if data.receive1:
            data3['total'] = data.receive1
        if data.receive2:
            data3['total'] += data.receive2
        if data.receive3:
            data3['total'] += data.receive3
        data3['totaln'] = -data3['total']
        data2 = Recovery.objects.get(id=pk)
    except:
        data = None
        data3 = None
        data2 = Recovery.objects.get(id=pk)
    return render(request, 'recovery/mgt_detail.html', {'data':data,'data2':data2, 'data3':data3})


def mgt_create(request, pk):

    data = Recovery.objects.get(id=pk)
    pk2 = data.car_data_id
    car = Data.objects.get(id=pk2)

    if request.method == 'POST':
        a = request.POST["aa"]
        b = request.POST["bb"]
        c = request.POST["cc"]
        d = request.POST["dd"]
        e = request.POST["ee"]
        f = request.POST["ff"]
        g = request.POST["gg"]
        h = request.POST["hh"]

        R_data_id = data.id
        car_num = data.car_num
        car_date = data.car_date

        if a == "":
            receive1 = None
        else:
            receive1 = a
        if b == "":
            redate1 = None
        else:
            redate1 = b
        if c == "":
            receive2 = None
        else:
            receive2 = c
        if d == "":
            redate2 = None
        else:
            redate2 = d
        if e == "":
            receive3 = None
        else:
            receive3 = e
        if f == "":
            redate3 = None
        else:
            redate3 = f
        if g == "":
            req_date = None
        else:
            req_date = g
        if h == "":
            req_cdate = None
        else:
            req_cdate = h
        save_data = RecoveryMgt(
            receive1=receive1,
            receive2=receive2,
            receive3=receive3,
            redate1=redate1,
            redate2=redate2,
            redate3=redate3,
            req_date=req_date,
            req_cdate=req_cdate,
            R_data_id=R_data_id,
            car_num=car_num,
            car_date=car_date
        )

        save_data.save()

        return redirect('recovery:mgt_detail', pk=pk)

    return render(request, 'recovery/mgt_create.html', {'data': data, 'car':car})


class MgtUpdatelView(UpdateView):
    model = RecoveryMgt
    fields = ['req_date', 'req_cdate', 'receive1', 'redate1', 'receive2', 'redate2', 'receive3', 'redate3']
    pk = RecoveryMgt.R_data
    success_url = "/recovery/0"
    template_name = 'recovery/mgt_update.html'

def mgt_delete(request, pk):
    data = RecoveryMgt.objects.get(R_data_id=pk)
    data.delete()

    return redirect('recovery:mgt_detail', pk=pk)

'''
from django.urls import reverse_lazy

class MgtlDetailView(DetailView):
    model = RecoveryMgt
    template_name = 'mgt_create'


class MgtCreateView(CreateView):
    model = RecoveryMgt
    fields = ['author', 'fdate', 'cus', 'car', 'num', 'spot', 'text']
    success_url = reverse_lazy('monitoring:mass_board')
    template_name = 'mgt_create'


class MgtUpdateView(UpdateView):
    model = RecoveryMgt
    fields = ['fdate', 'cus', 'car', 'num', 'spot', 'text']
    success_url = reverse_lazy('monitoring:mass_board')
    template_name = 'mgt_update'


class MgtDeleteView(DeleteView):
    model = RecoveryMgt
    success_url = reverse_lazy('monitoring:mass_board')
'''
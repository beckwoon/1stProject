from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from monitoring.models import *
from recovery.models import *

from datetime import datetime

@login_required

def remgt_board_st(request):
    today = datetime.now().date()
    year = today.year
    month = today.month
    day = today.day

    return redirect('remgt:remgt_board', year=year, month=month, day=day)


def remgt_board(request, year, month, day):
    date = str(year) + "-" + str(month) + "-" + str(day)
    if request.method == 'POST':
        date = request.POST["date"]
        sdate = datetime.strptime(date, "%Y-%m-%d").date()
        return redirect('remgt:remgt_board', year=sdate.year, month=sdate.month, day=sdate.day)
    else:
        sdate = datetime.strptime(date, "%Y-%m-%d").date()

    #print("########", date, type(date), sdate, type(sdate))

    datas = Data.objects.filter(a_rdate=sdate)
    cartypes = CarTypeMgt.objects.all()

    return render(request, "remgt/remgt_board.html", {'date':sdate, 'datas':datas, 'cartypes':cartypes})


def re_cus(request, pk):
    target = Data.objects.get(id=pk)
    try:
        remgt = ReManagement.objects.get(relink_id = pk)
        rdata = {}

        if remgt.cancel == True:
            rdata['cancel'] = "checked"
        elif remgt.cancel == False:
            rdata['cancel'] = "unchecked"
        rdata['mynum'] = remgt.myrepair_num
        rdata['mytotal'] = remgt.myrepair_price
        rdata['mymax'] = remgt.myrepair_max
        rdata['unum'] = remgt.urepair_num
        rdata['utotal'] = remgt.urepair_price
        rdata['umax'] = remgt.urepair_max
        rdata['spot'] = remgt.prespot

    except:
        rdata = {}

        rdata['cancel'] = "unchecked"
        rdata['mynum'] = 0
        rdata['mytotal'] = 0
        rdata['mymax'] = 0
        rdata['unum'] = 0
        rdata['utotal'] = 0
        rdata['umax'] = 0
        rdata['spot'] = None

    data = {}

    data['a_rdate'] = target.a_rdate
    data['car_num'] = target.car_num2
    data['car_num3'] = target.car_num3
    try:
        data['type'] = CarTypeMgt.objects.get(id=target.typelink_id).cartype
    except:
        data['type'] = None
    data['car_type'] = target.car_type
    data['car_model'] = target.car_model
    data['car_year'] = target.car_year
    data['car_sdate'] = target.car_sdate
    if target.cx == False:
        data['cx_name'] = '비인증'
    elif target.cx == True:
        data['cx_name'] = '인증'
    data['cus_name'] = target.cus_name
    data['cus_ctn'] = target.cus_ctn
    data['cus_add'] = target.cus_add
    data['cus_add2'] = target.cus_add2
    data['text'] = target.text

    cartypes = CarTypeMgt.objects.all()


    if request.method == 'POST':
        type_c = request.POST["type"]
        try:
            type = CarTypeMgt.objects.get(cartype=type_c)
        except:
            type = None
        year = request.POST["year"]
        sdate = request.POST["sdate"]
        cx_c = request.POST["cx"]
        if cx_c == "비인증" : cx = False
        elif cx_c == "인증" : cx = True
        name = request.POST["name"]
        ctn = request.POST["ctn"]
        add = request.POST["add"]
        add2_c = request.POST["add2"]
        add2 = add2_c.replace("/r/n","<br>")
        text_c = request.POST["text"]
        text = text_c.replace("/r/n","<br>")
        try:
            onoff = request.POST["cancel"]
            if onoff == "on": cancel = True
        except:
            cancel = False

        print("############", cancel)
        spot = request.POST["spot"]
        mynum = request.POST["num1"]
        mytotal = request.POST["mytotal"]
        mymax = request.POST["mymax"]
        unum = request.POST["num2"]
        utotal = request.POST["yourtotal"]
        umax = request.POST["yourmax"]


        target.typelink = type
        target.car_year = year
        target.car_sdate = sdate
        target.cx = cx
        target.cus_name = name
        target.cus_ctn = ctn
        target.cus_add = add
        target.cus_add2 = add2
        target.text = text

        target.save()

        try:
            remgt.cancel = cancel
            remgt.myrepair_num = mynum
            remgt.myrepair_price = mytotal
            remgt.myrepair_max = mymax
            remgt.urepair_num = unum
            remgt.urepair_price = utotal
            remgt.urepair_max = umax
            remgt.prespot = spot

            remgt.save()
        except:
            save_data = ReManagement(
                relink = target,
                car_num = target.car_num2,
                car_date = target.car_sdate,
                car_model = target.car_type,
                cancel = cancel,
                myrepair_num = mynum,
                myrepair_price = mytotal,
                myrepair_max = mymax,
                urepair_num = unum,
                urepair_price = utotal,
                urepair_max = umax,
                prespot = spot,
            )
            save_data.save()

        #print("############", cancel, spot, mynum, mytotal, mymax, unum, utotal, umax)

        return redirect('remgt:remgt_board', year=target.a_rdate.year, month=target.a_rdate.month, day=target.a_rdate.day)
    else:
        None


    return render(request, "remgt/re_cus.html", {'data':data, 'rdata':rdata, 'cartypes':cartypes, 'range':range(10)})

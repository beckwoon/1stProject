from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *


@login_required


def mibe_board(request):
    return render(request, 'monitoring/mibe_board.html')

def be_board(request):
    return render(request, 'monitoring/be_board.html')

from django.db.models import Q

def search_list(request):
    list = Data.objects.all()
    cnum = request.GET.get('number','')
    #print("##########", cnum)
    if cnum:
        list = list.filter(Q(car_num1__icontains=cnum) | Q(car_num2__icontains=cnum) | Q(car_num3__icontains=cnum))

    else:
        list = None
    return render(request, 'monitoring/data_list.html', {'list': list, 'cnum':cnum})

#class SearchListView(ListView):
#    model = Data
#    paginate_by = 5


class DataDetailView(DetailView):
    model = Data


class DataUpdatelView(UpdateView):
    model = Data
    fields = ['car_model', 'car_sdate', 'car_year', 'car_cor', 'car_price', 'ex', 'car_cor', 'car_ap', 'car_ap2', 'a_limm', 'car_acd', 'text']
    success_url = "/data/detail/{id}"
    template_name_suffix = '_update'


class MassListView(ListView):
    model = MassBoard
    paginate_by = 5


class MassCreateView(CreateView):
    model = MassBoard
    fields = ['author', 'fdate', 'cus', 'car', 'num', 'spot', 'text']
    success_url = reverse_lazy('monitoring:mass_board')
    template_name_suffix = '_create'


class MassUpdateView(UpdateView):
    model = MassBoard
    fields = ['fdate', 'cus', 'car', 'num', 'spot', 'text']
    success_url = reverse_lazy('monitoring:mass_board')
    template_name_suffix = '_update'


class MassDeleteView(DeleteView):
    model = MassBoard
    success_url = reverse_lazy('monitoring:mass_board')

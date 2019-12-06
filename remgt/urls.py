from django.urls import path
from .views import *

app_name = 'remgt'

urlpatterns=[
    path('', remgt_board_st, name='remgt_board_st'),
    path('re_cus/<int:pk>/', re_cus, name='re_cus'),
    path('<int:year>/<int:month>/<int:day>/', remgt_board, name='remgt_board'),
]
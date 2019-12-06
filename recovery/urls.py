from django.urls import path
from .views import *

app_name = 'recovery'

urlpatterns=[
    path('<int:mn>/', re_board, name='re_board'),
    path('create/<int:pk>/', recovery_create, name='re_create'),
    path('update/<int:pk>/', RecoveryUpdatelView.as_view(), name='re_update'),
    path('delete/<int:pk>/', recovery_delete, name='re_delete'),
    path('detail/<int:pk>/', recovery_detail, name='re_detail'),
    path('mgt/detail/<int:pk>/', mgt_detail, name='mgt_detail'),
    path('mgt/create/<int:pk>/', mgt_create, name='mgt_create'),
    path('mgt/update/<int:pk>/', MgtUpdatelView.as_view(), name='mgt_update'),
    path('mgt/delete/<int:pk>/', mgt_delete, name='mgt_delete'),
]
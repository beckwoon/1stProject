from django.urls import path
from .views import *
from .views2 import *
from .views3 import *

app_name = 'monitoring'

urlpatterns=[
    path('', ban_board, name='ban_board'),
    path('data/', search_list, name='search'),
    path('data/detail/<int:pk>/', DataDetailView.as_view(), name='detail'),
    path('data/update/<int:pk>/', DataUpdatelView.as_view(), name='data_update'),
    path('mass/', MassListView.as_view(), name='mass_board'),
    path('mass/add/', MassCreateView.as_view(), name='add'),
    path('mass/update/<int:pk>/', MassUpdateView.as_view(), name='update'),
    path('mass/delete/<int:pk>/', MassDeleteView.as_view(), name='delete'),
    #path('mi/', mibe_board, name='mibe_board'),
    #path('be/', be_board, name='be_board'),
    path('loading/', loading, name='loading')
]
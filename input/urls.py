from django.urls import path
from .views import *
from .models import Files

app_name = 'input'

urlpatterns=[
    path('', file_list, name='file_list'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
]
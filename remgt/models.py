from django.db import models
from monitoring.models import Data
# Create your models here.


class ReManagement(models.Model):
    relink = models.ForeignKey(Data, null=True, on_delete=models.CASCADE)
    car_num = models.CharField(max_length=10, null=True, verbose_name="차량번호")
    car_date = models.DateField(null=True, blank=True, verbose_name="반납일자")
    car_model = models.CharField(max_length=100, null=True, blank=True, verbose_name="모델")
    cancel = models.BooleanField(default=False, verbose_name="반납취소여부")
    myrepair_num = models.IntegerField(default=0, null=True, blank=True, verbose_name="내차 보험수리 횟수")
    myrepair_price = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="내차 보험수리 총액")
    myrepair_max = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="내차 보험수리 최고액")
    urepair_num = models.IntegerField(default=0, null=True, blank=True, verbose_name="타차 보험수리 횟수")
    urepair_price = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="타차 보험수리 총액")
    urepair_max = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="타차 보험수리 최고액")
    prespot = models.CharField(max_length=100, null=True, blank=True, verbose_name="반납예상지")
    created = models.DateTimeField(auto_now_add=True, verbose_name="등록일자")
    updated = models.DateTimeField(auto_now=True, verbose_name="수정일자")

    class Meta:
        ordering = ['created']
        verbose_name = '반납관리'
        verbose_name_plural = '반납관리'



from django.db import models
from monitoring.models import Data, MassBoard
# Create your models here.


class Recovery(models.Model):
    car_data = models.ForeignKey(Data, on_delete=models.PROTECT)
    car_num = models.CharField(max_length=10, null=True, verbose_name="차량번호")
    car_date = models.DateField(null=True, blank=True, verbose_name="반납일자")
    car_model = models.CharField(max_length=100, null=True, blank=True, verbose_name="모델")
    appraiser = models.CharField(max_length=10, null=True, blank=True, verbose_name="반납평가사")
    ap_grade = models.IntegerField(default=5, verbose_name="평가점수")
    rq_ex = models.BooleanField(default=False, verbose_name="보험접수유무")
    price_ex = models.BooleanField(default=False, verbose_name="일반수리유무")
    outstanding1 = models.BooleanField(default=False, verbose_name="보험미처리")
    outstanding2 = models.BooleanField(default=False, verbose_name="일반미처리")
    prog = models.BooleanField(default=False, verbose_name="미납처리")
    re_num = models.IntegerField(default=0, null=True, blank=True, verbose_name="원상회복건수")
    rp_num = models.IntegerField(default=0, null=True, blank=True, verbose_name="보험접수건수")
    re_part = models.CharField(max_length=100, null=True, blank=True, verbose_name="원상회복부위")
    rq_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="보험접수번호")
    rq_price = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="수리청구금액")
    cus_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="고객연락처")
    created = models.DateTimeField(auto_now_add=True, verbose_name="등록일자")
    text = models.TextField(blank=True, null=True, verbose_name="비고")

    class Meta:
        ordering = ['-created']
        verbose_name = '원상회복관리'
        verbose_name_plural = '원상회복관리'


class RecoveryMgt(models.Model):
    R_data = models.ForeignKey(Recovery, on_delete=models.CASCADE)
    car_num = models.CharField(max_length=10, null=True, verbose_name="차량번호")
    car_date = models.DateField(null=True, blank=True, verbose_name="반납일자")
    receive1 = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="입금액1")
    redate1 = models.DateField(blank=True, null=True, verbose_name="입금날짜1")
    receive2 = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="입금액2")
    redate2 = models.DateField(blank=True, null=True, verbose_name="입금날짜2")
    receive3 = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="입금액3")
    redate3 = models.DateField(blank=True, null=True, verbose_name="입금날짜3")
    receive4 = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="입금액4")
    redate4 = models.DateField(blank=True, null=True, verbose_name="입금날짜4")
    receive5 = models.BigIntegerField(default=0, null=True, blank=True, verbose_name="입금액5")
    redate5 = models.DateField(blank=True, null=True, verbose_name="입금날짜5")
    created = models.DateTimeField(auto_now_add=True, verbose_name="등록일자")
    updated = models.DateTimeField(auto_now=True, verbose_name="수정일자")
    req_date = models.DateField(blank=True, null=True, verbose_name="매입보류요청일")
    req_cdate = models.DateField(blank=True, null=True, verbose_name="보류해지요청일")

    class Meta:
        ordering = ['-created']


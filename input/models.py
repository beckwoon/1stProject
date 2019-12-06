from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

class Files(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_files')
    file = models.FileField(upload_to='반납데이터')
    text = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']
        verbose_name = 'file'
        verbose_name_plural = 'files'

    def __str__(self):
        return self.file.name + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('input:file_list', args=[str(self.id)])

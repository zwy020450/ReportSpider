from django.db import models
class Report(models.Model):
    objects = models.Manager()
    title=models.CharField(max_length=200)
    reporter=models.CharField(max_length=30)
    notice_time=models.CharField(max_length=30)
    report_time=models.CharField(max_length=30)
    address=models.CharField(max_length=60)
    link=models.CharField(max_length=300)
    university=models.CharField(max_length=30)
# Create your models here

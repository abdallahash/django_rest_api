from django.db import models

# Create your models here.

class File(models.Model):
    file_name = models.FileField(blank=False, null=False)
    remark = models.CharField(max_lenghth=40)
    timestamp = models.DateTimeField(auto_now_add=True)

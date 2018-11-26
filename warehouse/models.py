from django.db import models

# Create your models here.


class User(models.Model):
    account = models.CharField(max_length=20, primary_key=True, verbose_name="帐号")
    name = models.CharField(max_length=30, verbose_name="昵称")

    password = models.CharField(max_length=50)

    grade = models.IntegerField(default=0, verbose_name="权限")

    class Meta:
        verbose_name_plural = verbose_name = '用户管理'

    def __str__(self):
        return self.name

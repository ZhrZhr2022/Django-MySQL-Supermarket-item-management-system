from django.db import models


# Create your models here.
# python manage.py makemigrations
# python manage.py migrate

class User(models.Model):
    id = models.AutoField(verbose_name='用户编号', primary_key=True)
    phone_number = models.CharField(verbose_name='手机号', max_length=15)
    password = models.CharField(verbose_name='密码', max_length=100)
    balance = models.DecimalField(verbose_name='余额', max_digits=10, decimal_places=2)  # 用于存储精确的十进制数值
    picture = models.CharField(verbose_name='照片', max_length=255)  # 存放用户照片在服务器上的目录
    name = models.CharField(verbose_name='名字', max_length=10, default='')


class Goods(models.Model):
    id = models.AutoField(verbose_name='商品编号', primary_key=True)
    price = models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2)
    name = models.CharField(verbose_name='商品名称', max_length=100)
    count = models.IntegerField(verbose_name='商品数量')
    discount = models.DecimalField(verbose_name='商品折扣', max_digits=5, decimal_places=2, null=True, blank=True)
    introduce = models.CharField(verbose_name='商品介绍', max_length=3000)


class Codes(models.Model):
    id = models.AutoField(verbose_name='二维码编号', primary_key=True)
    code_id = models.IntegerField(verbose_name='二维码ID', default=-1)
    location = models.CharField(verbose_name='位置', max_length=50)


class Cars(models.Model):
    id = models.AutoField(verbose_name='购物车编号', primary_key=True)
    status = models.IntegerField(verbose_name='状态信息', default=0)  # 1表示被使用，0表示空闲


class Account(models.Model):
    """管理员账户表"""
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    id_choices = (
        (1, "管理员"),
    )
    identity = models.SmallIntegerField(verbose_name="身份", choices=id_choices, default=1)


class Tags(models.Model):
    id = models.AutoField(verbose_name='电子标签编号', primary_key=True)
    tag_id = models.CharField(verbose_name='电子标签号', max_length=64)
    goods_id = models.IntegerField(verbose_name='商品id')


class Codes_Tags(models.Model):
    id = models.AutoField(verbose_name='编号', primary_key=True)
    code_id = models.IntegerField(verbose_name='二维码ID')
    goods_id = models.IntegerField(verbose_name='商品id')

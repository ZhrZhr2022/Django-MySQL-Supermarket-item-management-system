import datetime

from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.encrypt import md5


class AccountModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:
        model = models.Account
        fields = ["username", "password", "confirm_password", "identity"]
        widgets = {
            "password": forms.PasswordInput
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        exist = models.Account.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exist:
            raise ValidationError("不能与之前的密码相同")
        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")
        confirm = md5(confirm)
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm


class Account1ModelForm(BootStrapModelForm):
    class Meta:
        model = models.Account
        fields = ["username", "identity"]


class Account2ModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:
        model = models.Account
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        exist = models.Account.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exist:
            raise ValidationError("不能与之前的密码相同")
        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")
        confirm = md5(confirm)
        if pwd != confirm:
            raise ValidationError("密码不一致")
        return confirm


class GoodsModelForm(BootStrapModelForm):
    class Meta:
        model = models.Goods
        fields = ["id", "price", "name", "count", "discount", "introduce"]

    def clean_goods_name(self):
        name_t = self.cleaned_data["name"]
        count1 = self.cleaned_data["count"]
        exists = models.Goods.objects.exclude(id=self.instance.pk).filter(name=name_t).exists()
        if exists:
            count_now = models.Goods.objects.filter(name=name_t).values('count').first()
            models.Goods.objects.filter(name=name_t).update(count=count1 + int(count_now["count"]))
        return name_t


class UserModelForm(BootStrapModelForm):
    # 校验手机号
    phone_number = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
    )

    class Meta:
        model = models.User
        fields = ["id", "phone_number", "password", "balance"]

    # 校验学生是否存在
    def clean_usr_id(self):
        txt_phone_number = self.cleaned_data["phone_number"]
        exists = models.User.objects.exclude(phone_number=self.instance.pk).filter(phone_number=txt_phone_number).exists()
        if exists:
            raise ValidationError("该学生已存在")
        return txt_phone_number


class CodesModelForm(BootStrapModelForm):
    class Meta:
        model = models.Codes
        fields = ["id", "location"]


class CarsModelForm(BootStrapModelForm):
    class Meta:
        model = models.Cars
        fields = ["id", "status"]

    def clean_car_id(self):
        txt_id = self.cleaned_data["id"]
        exists = models.Cars.objects.filter(id=txt_id).exists()
        if exists:
            raise ValidationError("该编号已存在")
        return txt_id


class TagsModelForm(BootStrapModelForm):
    class Meta:
        model = models.Tags
        fields = ["id", "tag_id", "goods_id"]

    def clean_tags_name(self):
        id_t = self.cleaned_data["id"]
        exists = models.Tags.objects.exclude(id=self.instance.pk).filter(id=id_t).exists()
        if exists:
            raise ValidationError("该编号已存在")
        return id_t

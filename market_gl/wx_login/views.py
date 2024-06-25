from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from app01 import models


class WechatView(APIView):

    def post(self, request, *args, **kwargs):
        # 获取 POST 请求中的数据
        data_POST = request.data
        phone_number = data_POST["username"]
        password = data_POST["password"]
        print(data_POST)
        data = models.User.objects.filter(phone_number=phone_number).first()
        if data is None:
            if data_POST["flag"] == 0:  # 登录
                return Response({"message": "no2"})
            elif data_POST["flag"] == 1:  # 注册
                if models.User.objects.create(phone_number=data_POST["username"], password=data_POST["password"], balance=0.0):
                    return Response({"message": "yes", "username": phone_number, "password": password})
                else:
                    return Response({"message": "no2", "username": phone_number, "password": password})
        else:
            if data_POST["flag"] == 0:  # 登录
                if data.password == password:
                    return Response({"message": "yes", "overage": data.balance, "username": phone_number, "password": password})
                else:
                    return Response({"message": "no1", "username": phone_number, "password": password})
            elif data_POST["flag"] == 1:  # 注册
                return Response({"message": "no1", "username": phone_number, "password": password})
            elif data_POST["flag"] == 2:  # 充值
                models.User.objects.filter(phone_number=phone_number).update(balance=data_POST["overage"])
                return Response({"message": "yes"})

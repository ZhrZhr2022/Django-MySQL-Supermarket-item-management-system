"""
WSGI config for market_gl project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market_gl.settings")
application = get_wsgi_application()

import socket
import threading
from app01 import models

username = '13399579409'
start_position = '0 0 0 0'
end_position = '1.269 -0.203 -0.689 0.725'

Pay_Flag = 0
rfid_flag = 1
Goods = []


def camera(conn, data):
    global username
    global Pay_Flag

    flag = int(data[1])
    if flag == 1:  # 登录人脸验证
        DB = models.User.objects.filter(name=data[2]).first()
        username = DB.phone_number
        if DB:
            conn.send("yes".encode("UTF-8"))
        else:
            conn.send("no".encode("UTF-8"))
    elif flag == 2:  # 扫码小车移动
        DB = models.Codes.objects.filter(code_id=int(data[2])).first()
        ToCar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ToCar.connect(("192.168.32.196", 8000))  # 需要改
        if DB:
            ToCar.send(("1 " + DB.location.strip()).encode("UTF-8"))  # 小车的数据解析需要更改
        ToCar.close()
    elif flag == 3:  # 停车
        ToCar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ToCar.connect(("192.168.32.196", 8000))  # 需要改
        ToCar.send(("1 " + end_position).encode('utf-8'))  # 小车的数据解析需要更改
        ToCar.close()

    elif flag == 4:  # 语音导航小车移动
        goods_codes = models.Codes_Tags.objects.filter(goods_id=int(data[2])).first()
        DB = models.Codes.objects.filter(code_id=int(goods_codes.code_id)).first()
        ToCar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ToCar.connect(("192.168.32.196", 8000))  # 需要改
        if DB:
            ToCar.send(("1 " + DB.location.strip()).encode("UTF-8"))  # 小车的数据解析需要更改
        ToCar.close()





def car():
    global Pay_Flag
    Pay_Flag = 1


def server_to_rfid():
    global Pay_Flag
    ip = "192.168.32.175"
    port = 8002
    server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2.bind((ip, port))
    server2.listen(5)
    conn, addr = server2.accept()
    while True:
        data = conn.recv(1024).decode("UTF-8").strip().split()

        flag = int(data[1])

        DB = models.Tags.objects.filter(tag_id=data[2].strip('\0').strip('\r').strip('\n')).first()
        goods = models.Goods.objects.filter(id=DB.goods_id).first()

        print(data)
        if goods:
            ToCamera = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ToCamera.connect(("192.168.32.15", 8001))  # 需要改
            if Pay_Flag == 1:
                models.Goods.objects.filter(id=DB.goods_id).update(count=goods.count - 1)
                user = models.User.objects.filter(phone_number=username).first()
                models.User.objects.filter(phone_number=username).update(balance=(user.balance - goods.price * goods.discount))
                Goods.remove(goods.name)
                print("value:" + str(goods.price * goods.discount))
                if len(Goods) == 0:
                    print("back")
                    ToCar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    ToCar.connect(("192.168.32.196", 8000))  # 需要改
                    ToCar.send(("1 " + start_position).encode("UTF-8"))  # 小车的数据解析需要更改
                    ToCar.close()
                    Pay_Flag = 0
                print(Goods)
            elif flag == 1:
                ToCamera.send(("1" + " " + goods.name + " " + str(goods.price) + " " + str(goods.discount)).encode("UTF-8"))  # 给板子发送
                Goods.append(goods.name)
                print(Goods)
                ToCamera.close()
            elif flag == 2:
                ToCamera.send(("2" + " " + goods.name + " " + str(goods.price) + " " + str(goods.discount)).encode("UTF-8"))
                Goods.remove(goods.name)
                print(Goods)
                ToCamera.close()

        if flag == 0:
            break

    conn.close()
    server2.close()




def server_test():
    global Pay_Flag
    global rfid_flag
    server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = "192.168.32.175"
    port = 8001
    server1.bind((ip, port))


    print("Server Started")
    while True:
        server1.listen(5)
        conn, addr = server1.accept()
        data = conn.recv(1024).decode("UTF-8")

        print("data:", data)

        data = data.strip().split()
        flag_id = int(data[0])
        if flag_id == 1:  # 板子
            camera(conn, data)

        elif flag_id == 3:
            car()

        conn.close()

        if data == "exit":
            break
    server1.close()


def ready():
    print("Ready method called")
    # 创建一个新线程来运行server_test()函数
    thread = threading.Thread(target=server_test)
    thread2 = threading.Thread(target=server_to_rfid)
    thread.daemon = True
    thread2.daemon = True  # 设置为守护线程，以确保在主线程结束时自动退出
    thread.start()
    thread2.start()


ready()


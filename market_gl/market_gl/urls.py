"""market_gl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app01.views import login1
from app01.views import account
from app01.views import goods
from app01.views import user
from app01.views import codes
from app01.views import car
from app01.views import tags
from wx_login import views

urlpatterns = [
    # # 默认访问登录页面
    path('', login1.login),

    # 登录
    path('login/', login1.login),
    # path('login1/', app.jiazai),
    path('logout/', login1.logout),
    # path('register/', login1.register),
    path('change/', account.change),

    # 管理员
    path('account/list/', account.account_list),
    path('account/add/', account.account_add),
    path('account/<int:nid>/edit1/', account.account_edit1),
    path('account/<int:nid>/edit2/', account.account_edit2),
    path('account/<int:nid>/delete/', account.account_delete),

    # 商品
    path('goods/list/', goods.goods_list),
    path('goods/add/', goods.goods_add),
    path('goods/<int:nid>/edit/', goods.goods_edit),
    path('goods/<int:nid>/delete/', goods.goods_delete),

    # 用户
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 二维码
    path('code/list/', codes.codes_list),
    path('code/add/', codes.codes_add),
    path('code/<int:nid>/edit/', codes.codes_edit),
    path('code/<int:nid>/delete/', codes.codes_delete),

    # 购物车
    path('car/list/', car.cars_list),
    path('car/add/', car.cars_add),
    path('car/<int:nid>/edit/', car.cars_edit),
    path('car/<int:nid>/delete/', car.cars_delete),

    # 标签
    path('tag/list/', tags.tags_list),
    path('tag/add/', tags.tags_add),
    path('tag/<int:nid>/edit/', tags.tags_edit),
    path('tag/<int:nid>/delete/', tags.tags_delete),

    # wechat
    path('wechat/login/', views.WechatView.as_view())
]

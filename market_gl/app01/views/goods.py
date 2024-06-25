from django.shortcuts import render, redirect
from django.contrib import messages
from app01 import models
from app01.utils.encrypt import md5
from app01.utils.pagination import Pagination
from app01.utils.form import GoodsModelForm


# Create your views here.


def goods_list(request):
    """ 商品列表 """
    data_dict = {}

    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.Goods.objects.filter(**data_dict).order_by("id")

    page_object = Pagination(request, queryset, page_size=15)

    context = {
        "search_date": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'goods_list.html', context)


def goods_add(request):
    """ 添加商品"""
    if request.method == "GET":
        form = GoodsModelForm()
        return render(request, 'goods_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = GoodsModelForm(data=request.POST)
    name1 = request.POST.get("name")

    if form.is_valid():
        # 如果数据合法，保存到数据库
        exist = models.Goods.objects.filter(name=name1).exists()
        if exist:
            form.clean_goods_name()
            message = "该商品已录入库中！数量已相加！"
            messages.success(request, message)  # 添加消息
            return redirect('/goods/list/')
        else:
            form.save()
            return redirect('/goods/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'goods_add.html', {"form": form})


def goods_edit(request, nid):
    # 编辑商品
    row_object = models.Goods.objects.filter(id=nid).first()
    if request.method == "GET":
        form = GoodsModelForm(instance=row_object)
        return render(request, 'goods_edit.html', {'form': form})

    form = GoodsModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/goods/list')

    return render(request, 'goods_edit.html', {"form": form})


def goods_delete(request, nid):
    # 删除
    models.Goods.objects.filter(id=nid).delete()
    return redirect("/goods/list/")

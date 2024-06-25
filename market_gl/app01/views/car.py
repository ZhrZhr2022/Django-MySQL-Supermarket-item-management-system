from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import CarsModelForm

# Create your views here.


def cars_list(request):
    """ 列表 """
    data_dict = {}

    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id__contains"] = search_data
    queryset = models.Cars.objects.filter(**data_dict).order_by("id")

    page_object = Pagination(request, queryset, page_size=15)

    context = {
        "search_date": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'cars_list.html', context)


def cars_add(request):
    """ 添加"""
    if request.method == "GET":
        form = CarsModelForm()
        return render(request, 'cars_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = CarsModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/car/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'cars_add.html', {"form": form})


def cars_edit(request, nid):
    # 编辑
    row_object = models.Cars.objects.filter(id=nid).first()
    if request.method == "GET":
        form = CarsModelForm(instance=row_object)
        return render(request, 'cars_edit.html', {'form': form})

    form = CarsModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/car/list')
    return render(request, 'cars_edit.html', {"form": form})


def cars_delete(request, nid):
    # 删除
    models.Cars.objects.filter(id=nid).delete()
    return redirect("/car/list/")

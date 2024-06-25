from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import CodesModelForm

# Create your views here.


def codes_list(request):
    """ 列表 """
    data_dict = {}

    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id__contains"] = search_data
    queryset = models.Codes.objects.filter(**data_dict).order_by("id")

    page_object = Pagination(request, queryset, page_size=15)

    context = {
        "search_date": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'codes_list.html', context)


def codes_add(request):
    """ 添加"""
    if request.method == "GET":
        form = CodesModelForm()
        return render(request, 'codes_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = CodesModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/code/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'codes_add.html', {"form": form})


def codes_edit(request, nid):
    # 编辑靓号
    row_object = models.Codes.objects.filter(id=nid).first()
    if request.method == "GET":
        form = CodesModelForm(instance=row_object)
        return render(request, 'codes_edit.html', {'form': form})

    form = CodesModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/code/list')
    return render(request, 'codes_edit.html', {"form": form})


def codes_delete(request, nid):
    # 删除
    models.Codes.objects.filter(id=nid).delete()
    return redirect("/code/list/")

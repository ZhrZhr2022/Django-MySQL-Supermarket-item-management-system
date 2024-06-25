from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import TagsModelForm


# Create your views here.


def tags_list(request):
    """ 商品列表 """
    data_dict = {}

    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id__contains"] = search_data
    queryset = models.Tags.objects.filter(**data_dict).order_by("id")

    page_object = Pagination(request, queryset, page_size=15)

    context = {
        "search_date": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'tags_list.html', context)


def tags_add(request):
    """ 添加商品"""
    if request.method == "GET":
        form = TagsModelForm()
        return render(request, 'tags_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = TagsModelForm(data=request.POST)

    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/tag/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'tags_add.html', {"form": form})


def tags_edit(request, nid):
    # 编辑商品
    row_object = models.Tags.objects.filter(id=nid).first()
    if request.method == "GET":
        form = TagsModelForm(instance=row_object)
        return render(request, 'tags_edit.html', {'form': form})

    form = TagsModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/tag/list')

    return render(request, 'tags_edit.html', {"form": form})


def tags_delete(request, nid):
    # 删除
    models.Tags.objects.filter(id=nid).delete()
    return redirect("/tag/list/")

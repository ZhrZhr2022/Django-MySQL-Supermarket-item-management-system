from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm

# Create your views here.


def user_list(request):
    """ 用户列表 """
    data_dict = {}

    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["phone_number__contains"] = search_data
    queryset = models.User.objects.filter(**data_dict).order_by("id")

    page_object = Pagination(request, queryset, page_size=15)

    context = {
        "search_date": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    return render(request, 'user_list.html', context)


def user_add(request):
    """ 添加用户"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        phone_number1 = request.POST.get("phone_number")
        exist = models.User.objects.filter(phone_number=phone_number1).exists()
        if exist:
            error_message = "该用户已存在！"
            return render(request, 'user_add.html', {"form": form, "error_message": error_message})
        else:
            form.save()
            return redirect('/user/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'user_add.html', {"form": form})


def user_edit(request, nid):
    # 编辑用户
    row_object = models.User.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    return render(request, 'user_edit.html', {"form": form})


def user_delete(request, nid):
    # 删除
    models.User.objects.filter(id=nid).delete()
    return redirect("/user/list/")

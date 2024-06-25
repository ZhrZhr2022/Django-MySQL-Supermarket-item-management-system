from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import AccountModelForm, Account1ModelForm, Account2ModelForm
from app01.utils.encrypt import md5


def account_list(request):
    """管理员列表"""
    data_dict = {}

    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data

    queryset = models.Account.objects.filter(**data_dict).order_by("username")
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data,
    }

    return render(request, 'account_list.html', context)


def account_add(request):
    """添加管理员"""
    if request.method == "GET":
        form = AccountModelForm()
        return render(request, 'account_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = AccountModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        form.save()
        return redirect('/account/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'account_add.html', {"form": form})


def account_edit1(request, nid):
    # 编辑管理员1
    row_object = models.Account.objects.filter(id=nid).first()
    if not row_object:
        # return render(request, 'error.html', {"msg": "数据不存在"})
        return redirect('/account/list')

    if request.method == "GET":
        form = Account1ModelForm(instance=row_object)
        return render(request, 'account_edit.html', {'form': form})

    form = Account1ModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/account/list')
    return render(request, 'account_edit.html', {"form": form})


def account_edit2(request, nid):
    # 编辑管理员2
    row_object = models.Account.objects.filter(id=nid).first()
    if not row_object:
        # return render(request, 'error.html', {"msg": "数据不存在"})
        return redirect('/account/list')

    if request.method == "GET":
        form = Account2ModelForm(instance=row_object)
        return render(request, 'account_edit.html', {'form': form})

    form = Account2ModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/account/list')
    return render(request, 'account_edit.html', {"form": form})


def account_delete(request, nid):
    # 删除
    models.Account.objects.filter(id=nid).delete()
    return redirect("/account/list/")


def change(request):
    if request.method == 'GET':
        form = Account2ModelForm()
        return render(request, 'change.html', {'form': form})

    form = Account2ModelForm(data=request.POST)
    username = request.POST.get("username")
    password = request.POST.get("password")
    password = md5(password)
    if form.is_valid():
        models.Account.objects.filter(username=username).update(password=password)
        return redirect('/login/')
    return render(request, 'change.html', {'form': form})


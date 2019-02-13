import hashlib
# import itchat
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app1 import models
from app1.models import User


def register(request):
    # 用户名username
    # 密码password
    # qq
    # email
    # tel
    # photo
    if request.method == "GET":
        return render(request, 'login_/register.html')
    elif request.method == "POST":
        username = request.POST.get("username")  # 接收用户名
        password = request.POST.get("password")  #
        qq = request.POST.get("qq")
        email = request.POST.get("email")
        tel = request.POST.get("tel")
        photo = request.FILES.get("photo")  # 接收头像

        new_user = User()
        new_user.username = username
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        new_user.password = md5.hexdigest()
        new_user.qq = qq
        new_user.email = email
        new_user.tel = tel
        if photo:
            new_user.photo = photo
        else:
            photo = '../static/uploads/morenphoto.jpg'
            new_user.photo = photo
        new_user.save()
        return redirect(reverse("transaction:login_"))


def login_(request):
    if request.method == "GET":
        return render(request, 'login_/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        password = md5.hexdigest()
        users = User.objects.filter(username=username, password=password)
        if users:
            user = users.first()
            request.session["user_id"] = user.id  # 登录成功后，设置session属性

            return redirect(reverse("transaction:person_center"))
        else:
            return redirect(reverse("transaction:login_"))


def check_username(request):
    username = request.GET.get('username')
    try:
        user = User.objects.get(username=username)
    except:
        data = {
            'status': '900',
            'msg': '该用户名可以被使用'
        }
        return JsonResponse(data)

    data = {
        'status': '901',
        'msg': '该用户名已被使用，请选择其他用户名！'
    }
    return JsonResponse(data)


def wechat_log(request):
    itchat.auto_login(hotReload=True)
    return redirect(reverse("transaction:person_center"))


def logout(request):
    request.session.flush()
    return redirect(reverse("transaction:person_center"))

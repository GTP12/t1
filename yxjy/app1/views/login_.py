import hashlib
import itchat
import re
import random

import http.client
import urllib

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app1 import models
from app1.models import User


def register(request):
    #用户名username
    #密码password
    #qq
    #email
    #tel
    #photo
    if request.method == "GET":
        return render(request,'login_/register.html')
    elif request.method == "POST":
        username = request.POST.get("username")  #接收用户名
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
            photo = '/uploads/morenphoto.jpg'
            new_user.photo = photo
        new_user.save()
        return redirect(reverse("transaction:login_"))

def login_(request):
    if request.method == "GET":
        return render(request,'login_/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        password = md5.hexdigest()
        users = User.objects.filter(username=username,password=password)
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
            'status':'900',
            'msg':'该用户名可以被使用'
        }
        return JsonResponse(data)

    data = {
        'status':'901',
        'msg':'该用户名已被使用，请选择其他用户名！'
    }
    return JsonResponse(data)

def wechat_log(request):

    itchat.login(picDir='')
    #picDir = ''
    user = itchat.get_friends()
    # 取出user中的第一段(即用户本人)的信息
    i = str(user[:1])
    print(i)
    info = i[8:-2]
    print(info)

    UserName = str(re.findall(r"'UserName': (.+?),", info))[2:-2]
    NickName = str(re.findall(r"'NickName': '(.+?)'", info))[2:-2]  # 昵称
    sign = str(re.findall(r"'Signature': '(.+?)'", info))[2:-2] # 签名
    sex = str(re.findall(r"'Sex': (.+?),", info))[2:-2]    # 1男  0女
    uin = str(re.findall(r"'Uin': (.+?),", info))[2:-2]
    img = str(re.findall(r"'HeadImgUrl': (.+?),", info))[2:-2]

    print(img)
    print(UserName)
    print(NickName)
    print(sign)
    print(sex)
    print(uin)
    username = uin
    password = uin
    qq = uin
    email = uin
    tel = uin
    photo = img
    new_user = User()
    new_user.username = username
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    new_user.password = md5.hexdigest()
    new_user.qq = qq
    new_user.email = email
    new_user.tel = tel
    new_user.photo = photo

    new_user.save()
    request.session["user_id"] = user.id
    return redirect(reverse("transaction:person_center"))


def logout(request):
    request.session.flush()
    return redirect(reverse("transaction:index"))

def send_sms(text, mobile):
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"

    # 用户名是登录用户中心->验证码短信->产品总览->APIID
    account = "C15457729"
    # 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
    password = "433251543855c87dd7fff2b12075ab59  "

    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

def yzm(request):
    tel = request.GET.get('tel')
    mobile = str(tel)
    print(mobile)
    num = str(random.randrange(1000, 9999))
    text = "您的验证码是：" + num + "。请不要把验证码泄露给其他人。"
    send_sms(text, mobile)
    return JsonResponse({'num': num})


def find_pwd(request):

    return render(request,'login_/find_pwd.html')




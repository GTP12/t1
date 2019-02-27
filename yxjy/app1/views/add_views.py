import datetime
import random
from app1.models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

app_name = 'transaction'

def account_deal(request):
    return render(request, 'account/account-deal.html')

def AddCount(request):
    if request.method =='GET':
        pass
    if request.method=='POST':
        pwd1=request.POST.get('pwd1')
        pwd2=request.POST.get('pwd2')
        areaname=request.POST.get('areaname')
        allareaname=Goldtypes.objects.filter(areaname=areaname)

        if allareaname:
            data={
                'status':'200',
                'msg':'输入正确'
            }
        elif  not allareaname:
            data={
                'status': '900',
                'msg': '请输入正确的大区信息'
            }
        if pwd1==pwd2 and pwd1:
            data = {
                'status': '200',
                'msg': '输入正确'
            }
        elif pwd1 != pwd2 and pwd1:
            data = {
                'status': '900',
                'msg': '两次密码输入不同，请重新输入'
            }


        return JsonResponse(data)



    return render(request, 'add/AddCount.html')


def success(request):
    if request.method=='POST':
        inputTitle = request.POST.get('inputTitle')
        print(inputTitle)
        price = request.POST.get('price')
        areaname_ = request.POST.get('parameters[54]')
        areid=Goldtypes.objects.get(areaname=areaname_).gameareaid
        account = request.POST.get('parameters[56]')
        password = request.POST.get('parameters[59]')
        name = request.POST.get('parameters[58]')
        qq = request.POST.get('qq')
        phone = request.POST.get('phone')
        qqleave = request.POST.get('parameters[59828]')
        if inputTitle and price and qq and password and phone:
            a = Account1()
            a.price = price
            a.sex = '男'
            a.gamearea = areaname_
            a.profession = name
            a.punish_record = '无五天封号记录'
            a.qq_grade = qqleave
            a.qq_friends = '无'
            a.safety_grade = 5
            a.publish_time = datetime.datetime.now()
            a.account_describe = inputTitle
            a.account_number = datetime.datetime.now().strftime('%Y%m%d')+str(random.randrange(1000,9999))
            a.state = 0
            a.user_id = 4
            a.expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
            a.gameareaid=areid
            a.save()
            return redirect(reverse('transaction:success'))

    return render(request, 'add/success.html')
def success2(request):
    if request.method=='POST':

        areaname_ = request.POST.get('parameters[54]')
        areid = Goldtypes.objects.get(areaname=areaname_).gameareaid
        password = request.POST.get('parameters[59]')
        material = request.POST.get('parameters[58]')
        materialid_ = Materialtypes.objects.get(materialsname=material).materialsid
        price = request.POST.get('price')
        num=request.POST.get('h1')
        stock=request.POST.get('stock')
        qq = request.POST.get('qq')
        phone = request.POST.get('phone')
        qqleave = request.POST.get('parameters[59828]')
        if material and price and qq and password and phone:
            a = Materials()
            a.price = price
            a.dealtype='材料'
            a.delivery='卖家发货'
            a.gamearea = areaname_
            a.meaterialsname = material
            a.gameareaid = areid
            a.goodinfo=str(num)+'个'+str(material)+'='+str(price)+'元'
            a.meaterialsid=materialid_

            a.goodsnum = stock
            a.datetime = datetime.datetime.now()

            a.productid = datetime.datetime.now().strftime('%Y%m%d')+str(random.randrange(1000,9999))
            a.state = 0
            a.user_id = 4
            # a.expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)

            a.save()
            return redirect(reverse('transaction:success'))

    return render(request, 'add/success.html')
def success3(request):
    if request.method=='POST':

        areaname_ = request.POST.get('parameters[54]')
        areid = Goldtypes.objects.get(areaname=areaname_).gameareaid
        password = request.POST.get('parameters[59]')
        price = request.POST.get('price')
        num=request.POST.get('h1')
        stock=request.POST.get('stock')
        qq = request.POST.get('qq')
        phone = request.POST.get('phone')
        qqleave = request.POST.get('parameters[59828]')
        if  price and qq and password and phone:
            a = Gold()
            a.price = price
            a.dealtype='游戏币'
            a.delivery='卖家发货'
            a.gamearea = areaname_

            a.gameareaid = areid
            a.goodinfo='【邮寄交易】 '+str(num)+'万游戏币'+'='+str(price)+'元'+'【即买即发，4396买卖零手续费 】'
            a.unitprice=int(num)/int(price)

            a.goodsnum = stock
            a.datetime = datetime.datetime.now()

            a.productid = datetime.datetime.now().strftime('%Y%m%d')+str(random.randrange(1000,9999))
            a.state = 0
            a.user_id = 4
            # a.expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)

            a.save()
            return redirect(reverse('transaction:success'))

    return render(request, 'add/success.html')

def success4(request):
    if request.method == 'POST':
        inputTitle=request.POST.get('inputTitle')#标题
        price=request.POST.get('price')
        description=request.POST.get('description')#账号需求描述
        areaname_ = request.POST.get('parameters[54]')
        areid = Goldtypes.objects.get(areaname=areaname_).gameareaid
        work=request.POST.get('parameters[02]') #职业
        qq = request.POST.get('qq')
        phone = request.POST.get('phone')
        qqleave = request.POST.get('parameters[59828]')
        if price and work and qq and phone:
            a=Account2()
            a.gamearea=areaname_
            a.sex='男'
            a.profession=work
            a.punish_record='无五天封号记录'
            a.qq_grade=qqleave
            a.qq_friends='无'
            a.account_message=inputTitle
            a.price=price
            a.publish_time = datetime.datetime.now()
            a.account_describe = inputTitle
            a.state = 0
            a.user_id = 4
            a.expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
            a.gameareaid = areid
            a.save()
            return redirect(reverse('transaction:success'))
    return render(request, 'add/success.html')
def gold_add(request):
    if request.method=='GET':
        pass
    if request.method=='POST':
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        areaname = request.POST.get('areaname')
        allareaname = Goldtypes.objects.filter(areaname=areaname)


        if allareaname:
            data = {
                'status': '200',
                'msg': '输入正确'
            }
        elif not allareaname:
            data = {
                'status': '900',
                'msg': '请输入正确的大区信息'
            }
        if pwd1 == pwd2 and pwd1:
            data = {
                'status': '200',
                'msg': '输入正确'
            }
        elif pwd1 != pwd2 and pwd1:
            data = {
                'status': '900',
                'msg': '两次密码输入不同，请重新输入'
            }
        return JsonResponse(data)

    return render(request, 'add/gold_add.html')

def stuff_add(request):
    if request.method=='GET':
        pass
    if request.method=='POST':
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        areaname = request.POST.get('areaname')
        allareaname = Goldtypes.objects.filter(areaname=areaname)
        material=request.POST.get('material')
        has_material=Materialtypes.objects.filter(materialsname=material)
        if allareaname:
            data = {
                'status': '200',
                'msg': '输入正确'
            }
        elif not allareaname:
            data = {
                'status': '900',
                'msg': '请输入正确的大区信息'
            }
        if pwd1 == pwd2 and pwd1:
            data = {
                'status': '200',
                'msg': '输入正确'
            }
        elif pwd1 != pwd2 and pwd1:
            data = {
                'status': '900',
                'msg': '两次密码输入不同，请重新输入'
            }
        if  has_material:
            data = {
                'status': '200',
                'msg': '输入正确'
            }
        elif not has_material and material:
            data = {
                'status': '900',
                'msg': '不存在该材料请重新输入'
            }
        return JsonResponse(data)
    return render(request, 'add/stuff_add.html')
def Add(request):
    return render(request, 'add/Add.html')
def add_buy(request):
    if request.method=='POST':
        areaname=request.POST.get('areaname')
        allareaname = Goldtypes.objects.filter(areaname=areaname)
        if allareaname:
            data = {
                'status': '200',
                'msg': '输入正确'
            }
        elif not allareaname:
            data = {
                'status': '900',
                'msg': '请输入正确的大区信息'
            }
        return JsonResponse(data)
    return render(request, 'add/add_buy.html')
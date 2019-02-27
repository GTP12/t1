import datetime
import random

from django.core.paginator import *
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template import loader

from app1.models import *

app_name = 'transaction'

def account_deal(request,area,page=1):
    game_type = Goldtypes.objects.all()
    if area ==10000:
        accounts = Account1.objects.filter(state=0)
    else:
        accounts = Account1.objects.filter(gameareaid=area,state=0)

    page_size =3
    paginator = Paginator(accounts,page_size)
    try:
        accounts = paginator.page(page)
    except PageNotAnInteger:
        accounts = paginator.page(1)
    return render(request,'account/account-deal.html',locals())


def account_order(request,id):
    a1 = Account1.objects.filter(id = id)
    account = a1[0]
    return render(request,'account/account-order.html',locals())


def deal_pay(request,id):


    a1 = Account1.objects.filter(id=id)
    account = a1[0]

    #更改账号表中账号的状态
    account.state = 1
    account.save()

    # sellorder表中买家订单信息生成
    sellorder = Sellorder1()
    sellorder.user_id=4

    sellorder.total_price = account.price
    sellorder.order_time = datetime.datetime.now()
    sellorder.order_num = 1
    sellorder.order_state =0
    sellorder.account1_id = id
    sellorder.order_tpye = "买家"
    sellorder.save()


    # sellorder2表中买家订单信息生成
    sellorder2 = Sellorder2()
    sellorder2.user_id =4 # sellorder.user = 4
    sellorder2.total_price = account.price
    sellorder2.order_time = datetime.datetime.now()
    sellorder2.order_num = 1
    sellorder2.order_state = 0
    sellorder2.account1_id= id
    sellorder2.order_tpye = "卖家"
    sellorder2.save()


    return render(request,'account/payment.html',locals())

def deal_success(request,id):

    #sellorder表中买家订单信息变更
    a1 = Account1.objects.filter(id=id)
    account = a1[0]
    s11 = Sellorder1.objects.filter(account1_id= id)
    s1 = s11[0]

    s1.order_state = 0
    s1.save()

    # sellorder2表中卖家订单信息变更
    s22 = Sellorder2.objects.filter(account1_id= id)
    s2 = s22[0]
    s2.order_state = 0
    s2.save()


    # moneymange表中身为卖家的资金明细
    user_id = account.user_id
    moneymanage= Moneymanage()
    m11= Moneymanage.objects.filter(user_id = user_id)
    n = len(m11)
    if n == 0:
        money_total =0
    else:
        m1 = m11[0]
        money_total = m1.mymoney
    moneymanage.user_id = user_id
    moneymanage.number = random.randrange(1000,10000)
    moneymanage.mymoney = money_total + account.price
    moneymanage.dealprice = account.price
    moneymanage.finishtime = datetime.datetime.now()
    moneymanage.dealstate = '1'
    moneymanage.save()

    #moneymange表中身为买家的资金明细
    user_id2 = 4
    moneymanage2 = Moneymanage()
    m22 = Moneymanage.objects.filter(user_id=user_id2)
    n = len(m22)
    if n == 0:
        money_total2 = 0
    else:
        m2 = m22[0]
        money_total2 = m2.mymoney
    moneymanage2.user_id = user_id2
    moneymanage2.mymoney = money_total2 - account.price
    moneymanage2.number = random.randrange(1000, 10000)
    moneymanage2.dealprice = -account.price
    moneymanage2.finishtime = datetime.datetime.now()
    moneymanage2.dealstate = '1'
    moneymanage2.save()

    return render(request,'pay/paysuccess.html')


def account_purchase(request,area,page=1):
    game_type = Goldtypes.objects.all()
    if area == 10000:
        accounts = Account2.objects.filter(state=0)
    else:
        accounts = Account2.objects.filter(gameareaid=area,state=0)

    page_size = 3
    paginator = Paginator(accounts, page_size)
    try:
        accounts = paginator.page(page)
    except PageNotAnInteger:
        accounts = paginator.page(1)
    return render(request,'account/account-purchase.html',locals())


def account_order2(request,id):
    account2_id = id

    return render(request,'account/account-order2.html',locals())


def details3(request,id):
    a1 = Account1.objects.filter(id = id)
    account = a1[0]


    return render(request,'account/details3.html',locals())

def success_(request,id):
    #接收表单上传的数据，并且写入purchasemessage表中
    account_number = request.POST.get('account_number')
    pwd = request.POST.get('password')
    purchasemessage = Purchasemessage()
    purchasemessage.game_account = account_number
    purchasemessage.account_pwd = pwd
    purchasemessage.account2_id = id

    purchasemessage.user_id = 4  #purchasemessage.user_id = request.id
    purchasemessage.save()


    a2 = Account2.objects.filter(id=id)
    account2 = a2[0]

    #修改求购账号表中的账号状态
    account2.state = 1
    account2.save()

    # 买家账号求购订单表的数据
    price = account2.price
    purchaseorder1 = Purchaseorder1()
    purchaseorder1.account2_id = id
    purchaseorder1.user_id = 4 #purchaseorder1.user_id = 4
    purchaseorder1.order_time = datetime.datetime.now()
    purchaseorder1.order_state = 0
    purchaseorder1.total_price = price
    purchaseorder1.order_num = 1
    purchaseorder1.order_tpye = 0
    purchaseorder1.save()

    # 卖家账号求购订单表的数据
    purchaseorder2 = Purchaseorder2()
    purchaseorder2.account2_id = id
    purchaseorder2.user_id = 4  # purchaseorder2.user_id = 4
    purchaseorder2.order_time = datetime.datetime.now()
    purchaseorder2.order_state = 0
    purchaseorder2.total_price = price
    purchaseorder2.order_num = 1
    purchaseorder2.order_tpye = 1
    purchaseorder2.save()

    # moneymange表中身为卖家的资金明细
    user_id=4   #user_id = 4_id
    moneymanage = Moneymanage()
    m22 = Moneymanage.objects.filter(user_id=user_id)
    n = len(m22)
    if n ==0:
        money_total =0
    else:
        m1 = m22[0]
        money_total = m1.mymoney
    moneymanage.user_id = user_id
    moneymanage.number = random.randrange(1000, 10000)
    moneymanage.mymoney = money_total + price
    moneymanage.dealprice = price
    moneymanage.finishtime = datetime.datetime.now()
    moneymanage.dealstate = '1'
    moneymanage.save()



    # moneymange表中身为买家的资金明细
    user_id2 = account2.user_id
    moneymanage2 = Moneymanage()
    m33 = Moneymanage.objects.filter(user_id=user_id2)
    n = len(m33)
    if n == 0:
        money_total2 = 0
    else:
        m2 = m33[n - 1]
        money_total2 = m2.mymoney
    moneymanage2.user_id = user_id2
    moneymanage2.number = random.randrange(1000, 10000)
    moneymanage2.mymoney = money_total2 - price
    moneymanage2.dealprice = -price
    moneymanage2.finishtime = datetime.datetime.now()
    moneymanage2.dealstate = '1'
    moneymanage2.save()


    return render(request,'account/success_.html')

#账号出售页面

#价格从大到小排序
def sort_price1(request):
    id = request.GET.get('top')
    if id == '10000':
        accounts = Account1.objects.all()
    else:
        accounts = Account1.objects.filter(gameareaid=int(id))
    accounts = accounts.order_by('-price')
    html = loader.render_to_string("account/sort_.html", locals())
    return HttpResponse(html)


#价格从小到大排序
def sort_price2(request):
    id = request.GET.get('top')
    if id == '10000':
        accounts = Account1.objects.all()
    else:
        accounts = Account1.objects.filter(gameareaid=int(id))
    accounts = accounts.order_by('price')
    html = loader.render_to_string("account/sort_.html", locals())
    return HttpResponse(html)

#日期从大到小
def sort_time1(request):
    id = request.GET.get('top')
    if id == '10000':
        accounts = Account1.objects.all()
    else:
        accounts = Account1.objects.filter(gameareaid=int(id))
    accounts = accounts.order_by('-publish_time')
    html = loader.render_to_string("account/sort_.html", locals())
    return HttpResponse(html)

#日期从小到大
def sort_time2(request):
    id = request.GET.get('top')
    if id == '10000':
        accounts = Account1.objects.all()
    else:
        accounts = Account1.objects.filter(gameareaid=int(id))
    accounts = accounts.order_by('publish_time')
    html = loader.render_to_string("account/sort_.html", locals())
    return HttpResponse(html)

#关键字和价格查询查询
def search_(request,area,page=1):

    game_type = Goldtypes.objects.all()
    key = request.GET.get('keywords')  # 关键字查询
    minprice = request.GET.get('minPrice')
    maxprice = request.GET.get('maxPrice')
    if not key and minprice and maxprice:
        minprice = float(minprice)
        maxprice = float(maxprice)
        if minprice > maxprice:
            minprice, maxprice = maxprice, minprice
        q1 = Q(price__gte=minprice)
        q2 = Q(price__lte=maxprice)
        accounts = Account1.objects.filter(q1 & q2)
    elif key and not minprice and not maxprice:
        accounts = Account1.objects.filter(account_describe__contains=key)
    elif key and maxprice and minprice:
        minprice = float(minprice)
        maxprice = float(maxprice)
        if minprice > maxprice:
            minprice, maxprice = maxprice, minprice
        q1 = Q(price__gte=minprice)
        q2 = Q(price__lte=maxprice)
        q3 = Q(account_describe__contains=key)
        accounts = Account1.objects.filter(q1 & q2 & q3)
    else:
        accounts = Account1.objects.all()
    page_size = 4
    paginator = Paginator(accounts, page_size)
    try:
        golds = paginator.page(page)
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时，显示第一页
        golds = paginator.page(1)
    except EmptyPage:
        golds = paginator.page(paginator.num_pages)  # 最后一页
    return render(request, 'account/account-deal.html', locals())

# 求购页面搜索
def search_2(request,area,page=1):

    game_type = Goldtypes.objects.all()
    key = request.GET.get('keywords')  # 关键字查询
    minprice = request.GET.get('minPrice')
    maxprice = request.GET.get('maxPrice')
    if not key and minprice and maxprice:
        minprice = float(minprice)
        maxprice = float(maxprice)
        if minprice > maxprice:
            minprice, maxprice = maxprice, minprice
        q1 = Q(price__gte=minprice)
        q2 = Q(price__lte=maxprice)
        accounts = Account2.objects.filter(q1 & q2)
    elif key and not minprice and not maxprice:
        accounts = Account2.objects.filter(account_message__contains=key)
    elif key and maxprice and minprice:
        minprice = float(minprice)
        maxprice = float(maxprice)
        if minprice > maxprice:
            minprice, maxprice = maxprice, minprice
        q1 = Q(price__gte=minprice)
        q2 = Q(price__lte=maxprice)
        q3 = Q(account_message__contains=key)
        accounts = Account2.objects.filter(q1 & q2 & q3)
    else:
        accounts = Account2.objects.all()
    page_size = 4
    paginator = Paginator(accounts, page_size)
    try:
        golds = paginator.page(page)
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时，显示第一页
        golds = paginator.page(1)
    except EmptyPage:
        golds = paginator.page(paginator.num_pages)  # 最后一页
    return render(request, 'account/account-purchase.html', locals())


#账号求购页面排序

#价格从大到小排序
def sort_price3(request):
    id = request.GET.get('top')
    if id == '10000':
        accounts = Account2.objects.all()
    else:
        accounts = Account2.objects.filter(gameareaid=int(id))
    accounts = accounts.order_by('-price')
    html = loader.render_to_string("account/sort_2.html", locals())
    return HttpResponse(html)


#价格从小到大排序
def sort_price4(request):
    id = request.GET.get('top')
    if id == '10000':
        accounts = Account2.objects.all()
    else:
        accounts = Account2.objects.filter(gameareaid=int(id))
    accounts = accounts.order_by('price')
    html = loader.render_to_string("account/sort_2.html", locals())
    return HttpResponse(html)

#日期从大到小
def sort_time3(request):
    id = request.GET.get('top')
    if id == '10000':
        accounts = Account2.objects.all()
    else:
        accounts = Account2.objects.filter(gameareaid=int(id))
    accounts = accounts.order_by('-publish_time')
    a1 = accounts[0]
    print(a1.price)
    html = loader.render_to_string("account/sort_2.html", locals())
    return HttpResponse(html)

#日期从小到大
def sort_time4(request):
    id = request.GET.get('top')
    if id == '10000':
        accounts = Account2.objects.all()
    else:
        accounts = Account2.objects.filter(gameareaid=int(id))
    accounts = accounts.order_by('publish_time')
    html = loader.render_to_string("account/sort_2.html", locals())
    return HttpResponse(html)
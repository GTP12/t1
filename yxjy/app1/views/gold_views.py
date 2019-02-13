import datetime
import random
import re

from django.core.paginator import *
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from app1.models import *

app_name = 'transaction'


# 金币购买页面
def gold_deal(request, area, page=1):
    # 所在区显示
    game_type = Goldtypes.objects.all()
    if area == 10000:
        golds = Gold.objects.all()
    else:
        golds = Gold.objects.filter(gameareaid=area)
    # 分页管理
    page_size = 4  # 每页显示4条数据
    paginator = Paginator(golds, page_size)
    try:
        golds = paginator.page(page)
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时，显示第一页
        golds = paginator.page(1)
    except EmptyPage:
        golds = paginator.page(paginator.num_pages)  # 最后一页
    return render(request, 'gold/gold-deal.html', locals())


def gold_key(request, area, page=1):
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
        golds = Gold.objects.filter(q1 & q2)
    elif key and not minprice and not maxprice:
        golds = Gold.objects.filter(goodinfo__contains=key)
    elif key and maxprice and minprice:
        minprice = float(minprice)
        maxprice = float(maxprice)
        if minprice > maxprice:
            minprice, maxprice = maxprice, minprice
        q1 = Q(price__gte=minprice)
        q2 = Q(price__lte=maxprice)
        q3 = Q(goodinfo__contains=key)
        golds = Gold.objects.filter(q1 & q2 & q3)
    else:
        golds = Gold.objects.all()
    page_size = 20  # 每页显示4条数据
    paginator = Paginator(golds, page_size)
    try:
        golds = paginator.page(page)
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时，显示第一页
        golds = paginator.page(1)
    except EmptyPage:
        golds = paginator.page(paginator.num_pages)  # 最后一页
    return render(request, 'gold/gold-deal.html', locals())


# 金币商品详情页面
def gold_details(request, id):
    gold = Gold.objects.get(id=id)
    # 商品推荐
    goods = Gold.objects.filter(gamearea=gold.gamearea)
    goods = goods[:5]
    # 商家信誉表
    good = Gold.objects.get(id=id)
    user = User.objects.get(id=good.user_id)
    credit = Credit.objects.get(id=user.id)
    return render(request, 'gold/gold-details.html', locals())


# 购买商品
def gold_purchase(request, id):
    if request.method == 'GET':
        # 确认商品
        gold = Gold.objects.get(id=id)
        # 单价
        price = round(gold.unitprice / gold.price, 4)
        # 交易方式：
        trading = gold.goodinfo[1:5]
        return render(request, 'gold/goldPurchase.html', locals())
    else:
        num = request.POST.get('num')
        trading = request.POST.get('trading')
        reaparea = request.POST.get('reaparea')
        tel = request.POST.get('phone')
        qq = request.POST.get('qq')
        payprice = request.POST.get('payprice')
        gold_id = id
        ordernumber = (datetime.datetime.now()).strftime('%Y%m%d') + str(random.randrange(1000, 9999))
        goldorder = Goldorder(num=num, trading=trading, reaparea=reaparea, tel=tel, qq=qq, payprice=payprice,
                              gold_id=gold_id, ordernumber=ordernumber)
        goldorder.save()
        # 订单信息
        order_time = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        order_state = 1
        """
        
        """
        order_type = 1  # '拍卖交易'
        goldsorder2 = Goldorder2(gold_id=gold_id, user_id=1, order_time=order_time, order_state=order_state,
                                 total_price=payprice, order_num=ordernumber, order_tpye=order_type)
        """
        1  交易中
        0  交易成功
        2  交易失败
        """
        goldsorder2.save()
        return redirect(reverse('transaction:payment', args=(payprice, order_time)))


# 判断手机号是否正确
def check_phone(request):
    phone = request.GET.get('phone')
    ret = re.match(r"^1[35678]\d{9}$", phone)
    if not ret:
        data = {
            "color": 'red',
            "msg": '请输入正确的号码！',
            "status": 'fail'}
        return JsonResponse(data)
    return JsonResponse(data={"coloe": "",
                              "msg": '',
                              'status': ''})


# 验证qq号码是否正确
def check_qq(request):
    qq = request.GET.get('qq')
    ret = re.match(r"^[0-9]{5,12}$", qq)
    if not ret:
        data = {
            "color": 'red',
            "msg": 'qq号码错误！',
            "status": 'fail'}
        return JsonResponse(data)
    return JsonResponse(data={"coloe": "",
                              "msg": '',
                              'status': ''})


# 价格从大到小排序
def check_maxprice(request):
    id = request.GET.get('top')
    if id == '10000':
        goods = Gold.objects.all()
    else:
        goods = Gold.objects.filter(gameareaid=int(id))
    goods = goods.order_by('-price')
    html = loader.render_to_string("gold/goldprice.html", locals())
    return HttpResponse(html)


# 价格从小到大排序
def check_minprice(request):
    path = request.path
    id = request.GET.get('top')
    if id == '10000':
        goods = Gold.objects.all()
    else:
        goods = Gold.objects.filter(gameareaid=int(id))
    goods = goods.order_by('price')
    html = loader.render_to_string("gold/goldprice.html", locals())
    return HttpResponse(html)


# 日期从大到小排序
def check_maxtime(request):
    id = request.GET.get('top')
    if id == '10000':
        goods = Gold.objects.all()
    else:
        goods = Gold.objects.filter(gameareaid=int(id))
    goods = goods.order_by('-datetime')

    html = loader.render_to_string("gold/goldprice.html", locals())
    return HttpResponse(html)


# 日期价格从小到大排序
def check_mintime(request):
    id = request.GET.get('top')
    if id == '10000':
        goods = Gold.objects.all()
    else:
        goods = Gold.objects.filter(gameareaid=int(id))
    goods = goods.order_by('datetime')
    html = loader.render_to_string("gold/goldprice.html", locals())
    return HttpResponse(html)


# 默认排序
def check_default(request):
    id = request.GET.get('top')
    if id == '10000':
        goods = Gold.objects.all()
    else:
        goods = Gold.objects.filter(gameareaid=int(id))
    goods = goods.order_by('id')
    html = loader.render_to_string("gold/goldprice.html", locals())
    return HttpResponse(html)


# 验证价格
def check_stock(request):
    stock = request.GET.get('stock')
    price = request.GET.get('price')
    print(stock,price)

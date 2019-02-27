import datetime
import random
import re

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from app1.models import *

app_name = 'transaction'


# 材料购买页面
def material_deal(request, area, materialid, page=1):
    # 所在区和材料类型显示
    game_type = Goldtypes.objects.all()
    game_materials = Materialtypes.objects.all()
    if area == 10000 and materialid == 20000:
        materials = Materials.objects.all()
    elif area == 10000 and materialid != 20000:
        materials = Materials.objects.filter(meaterialsid=materialid)
    elif area != 10000 and materialid == 20000:
        materials = Materials.objects.filter(gameareaid=area)
    else:
        materials = Materials.objects.filter(gameareaid=area, meaterialsid=materialid)
    # 选择对应材料显示对应的数据
    child_dict = {}
    goldtypes = Goldtypes.objects.get(gameareaid=area)
    childnames = goldtypes.childtypenames
    childlist = childnames.split('#')
    for child in childlist:
        temp = child.split(':')
        child_dict[temp[0]] = int(temp[1])
    # 分页管理
    page_size = 5  # 每页显示4条数据
    paginator = Paginator(materials, page_size)
    try:
        materials = paginator.page(page)
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时，显示第一页
        materials = paginator.page(1)
    except EmptyPage:
        materials = paginator.page(paginator.num_pages)  # 最后一页
    return render(request, 'material/material-deal.html', locals())


# 材料商品详情表
def details2(request, id):
    material = Materials.objects.get(id=id)
    # 商品推荐
    materials = Materials.objects.filter(gamearea=material.gamearea)
    materials = materials[:5]
    # 卖家信誉
    good = Materials.objects.get(id=id)
    user = User.objects.get(id=good.user_id)
    credit = Credit.objects.get(id=user.id)
    return render(request, 'material/details2.html', locals())


# 关键字搜索
def material_key(request, area, materialid, page=1):
    game_type = Goldtypes.objects.all()
    child_dict = {}
    goldtypes = Goldtypes.objects.get(gameareaid=area)
    childnames = goldtypes.childtypenames
    childlist = childnames.split('#')
    for child in childlist:
        temp = child.split(':')
        child_dict[temp[0]] = int(temp[1])
    key = request.GET.get('keywords')  # 关键字查询
    print(key)
    minprice = request.GET.get('minPrice')
    maxprice = request.GET.get('maxPrice')
    if not key and minprice and maxprice:
        minprice = float(minprice)
        maxprice = float(maxprice)
        if minprice > maxprice:
            minprice, maxprice = maxprice, minprice
        q1 = Q(price__gte=minprice)
        q2 = Q(price__lte=maxprice)
        materials = Materials.objects.filter(q1 & q2)
    elif key and not minprice and not maxprice:
        materials = Materials.objects.filter(goodinfo__contains=key)
    elif key and maxprice and minprice:
        minprice = float(minprice)
        maxprice = float(maxprice)
        if minprice > maxprice:
            minprice, maxprice = maxprice, minprice
        q1 = Q(price__gte=minprice)
        q2 = Q(price__lte=maxprice)
        q3 = Q(goodinfo__contains=key)
        materials = Materials.objects.filter(q1 & q2 & q3)
    else:
        materials = Materials.objects.all()
    page_size = 20  # 每页显示4条数据
    paginator = Paginator(materials, page_size)
    try:
        golds = paginator.page(page)
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时，显示第一页
        golds = paginator.page(1)
    except EmptyPage:
        golds = paginator.page(paginator.num_pages)  # 最后一页
    return render(request, 'material/material-deal.html', locals())


# 材料购买
def material_purchase(request, id):
    if request.method == 'GET':
        material = Materials.objects.get(id=id)
        # 交易方式
        return render(request, 'material/materialPurchase.html', locals())
    else:
        num = request.POST.get('num')
        trading = request.POST.get('trading')
        rolename = request.POST.get('rolename')
        reaparea = request.POST.get('reaparea')
        tel = request.POST.get('phone')
        qq = request.POST.get('qq')
        payprice = request.POST.get('payprice')
        material_id = id
        ordernumber = (datetime.datetime.now()).strftime('%Y%m%d') + str(random.randrange(1000, 9999))
        materialorder = Materialsorder(num=num, reaparea=reaparea, tel=tel, qq=qq, payprice=payprice,
                                       materials_id=material_id, ordernumber=ordernumber, rolename=rolename)
        materialorder.save()
        # 材料交易买方订单表
        order_time = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        order_state = 1
        """

        """
        order_type = 1  # '拍卖交易'
        materialsorder = Materialsorder2(materials_id=material_id, user_id=1, order_time=order_time,
                                         order_state=order_state,total_price=payprice, order_num=ordernumber,
                                         order_tpye=order_type)
        """
        1  交易中
        0  交易成功
        2  交易失败
        """
        materialsorder.save()
        return redirect(reverse('transaction:payment', args=(payprice, order_time)))


# 验证输入购买材料数量是否合理
def check_num(request):
    num = request.GET.get('num')
    ret = re.match(r"^[0-9]$\d*", num)
    price = request.GET.get('prices')
    if price:
        if ret:
            if num == '0':
                data = {
                    "color": 'red',
                    "msg": '数量不能为0！',
                    "status": 'fail',
                    "price": price}
                return JsonResponse(data)
            price = round(float(price) * int(num), 2)
            return JsonResponse(data={"coloe": "",
                                      "msg": '',
                                      'status': '',
                                      'num': num,
                                      'price': price})
        else:
            data = {
                "color": 'red',
                "msg": '输入错误，请重新输入！',
                "status": 'fail',
                "num": 1,
                "price": price}
        return JsonResponse(data)


# 价格从大到小排序
def check_matrial_maxprice(request):
    gameid = request.GET.get('gameid')
    matid = request.GET.get('matid')
    if gameid == '10000' and matid == '20000':
        goods = Materials.objects.all()
    elif gameid == '10000' and matid != '20000':
        goods = Materials.objects.filter(meaterialsid=int(matid))
    elif gameid != '10000' and matid == '20000':
        goods = Materials.objects.filter(gameareaid=int(gameid))
    else:
        goods = Materials.objects.filter(gameareaid=int(gameid), meaterialsid=int(matid))
    goods = goods.order_by('-price')
    html = loader.render_to_string("material/matialprice.html", locals())
    return HttpResponse(html)


# # 价格从小到大排序
def check_matrial_minprice(request):
    gameid = request.GET.get('gameid')
    matid = request.GET.get('matid')
    if gameid == '10000' and matid == '20000':
        goods = Materials.objects.all()
    elif gameid == '10000' and matid != '20000':
        goods = Materials.objects.filter(meaterialsid=int(matid))
    elif gameid != '10000' and matid == '20000':
        goods = Materials.objects.filter(gameareaid=int(gameid))
    else:
        goods = Materials.objects.filter(gameareaid=int(gameid), meaterialsid=int(matid))
    goods = goods.order_by('price')
    html = loader.render_to_string("material/matialprice.html", locals())
    return HttpResponse(html)


# # 日期从大到小排序
def check_matrial_maxtime(request):
    gameid = request.GET.get('gameid')
    matid = request.GET.get('matid')
    if gameid == '10000' and matid == '20000':
        goods = Materials.objects.all()
    elif gameid == '10000' and matid != '20000':
        goods = Materials.objects.filter(meaterialsid=int(matid))
    elif gameid != '10000' and matid == '20000':
        goods = Materials.objects.filter(gameareaid=int(gameid))
    else:
        goods = Materials.objects.filter(gameareaid=int(gameid), meaterialsid=int(matid))
    goods = goods.order_by('-datetime')
    html = loader.render_to_string("material/matialprice.html", locals())
    return HttpResponse(html)


# # 日期价格从小到大排序
def check_matrial_mintime(request):
    gameid = request.GET.get('gameid')
    matid = request.GET.get('matid')
    if gameid == '10000' and matid == '20000':
        goods = Materials.objects.all()
    elif gameid == '10000' and matid != '20000':
        goods = Materials.objects.filter(meaterialsid=int(matid))
    elif gameid != '10000' and matid == '20000':
        goods = Materials.objects.filter(gameareaid=int(gameid))
    else:
        goods = Materials.objects.filter(gameareaid=int(gameid), meaterialsid=int(matid))
    goods = goods.order_by('datetime')
    html = loader.render_to_string("material/matialprice.html", locals())
    return HttpResponse(html)


# # 默认排序
def check_matrial_default(request):
    gameid = request.GET.get('gameid')
    matid = request.GET.get('matid')
    if gameid == '10000' and matid == '20000':
        goods = Materials.objects.all()
    elif gameid == '10000' and matid != '20000':
        goods = Materials.objects.filter(materialid=int(matid))
    elif gameid != '10000' and matid == '20000':
        goods = Materials.objects.filter(gameareaid=int(gameid))
    else:
        goods = Materials.objects.filter(gameareaid=int(gameid), meaterialsid=int(matid))
    goods = goods.order_by('id')
    html = loader.render_to_string("material/matialprice.html", locals())
    return HttpResponse(html)

#
# # 验证价格
# def check_stock(request):
#     stock = request.GET.get('stock')
#     price = request.GET.get('price')
#     print(stock,price)
#

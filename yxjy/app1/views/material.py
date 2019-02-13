import datetime
import random
import re

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app1.models import *

app_name = 'transaction'


# 材料购买页面
def material_deal(request, area, materialid, page=1):
    # 所在区和材料类型显示
    game_type = Goldtypes.objects.all()
    game_materials = Materialtypes.objects.all()
    if area == 10000 :
        materials = Materials.objects.all()
    else:
        materials = Materials.objects.filter(gameareaid=area)

        # 分页管理
    page_size = 6  # 每页显示4条数据
    paginator = Paginator(materials, page_size)
    try:
        golds = paginator.page(page)
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时，显示第一页
        golds = paginator.page(1)
    except EmptyPage:
        golds = paginator.page(paginator.num_pages)  # 最后一页
    return render(request, 'material/material-deal.html', locals())


# 材料商品详情表
def details2(request, id):
    material = Materials.objects.get(id=id)
    # 商品推荐
    materials = Materials.objects.filter(gamearea=material.gamearea)
    materials = materials[:5]
    return render(request, 'material/details2.html', locals())


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
        materialsorder = goldorder2 = Materialsorder2(materials_id=material_id, user_id=1, order_time=order_time,
                                                      order_state=order_state,
                                                      total_price=payprice, order_num=ordernumber,
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
    if ret:
        if num == '0':
            data = {
                "color": 'red',
                "msg": '数量不能为0！',
                "status": 'fail',
                "num": 1}
            return JsonResponse(data)
        return JsonResponse(data={"coloe": "",
                                  "msg": '',
                                  'status': '',
                                  'num': num})
    else:
        data = {
            "color": 'red',
            "msg": '输入数量错误！',
            "status": 'fail',
            "num": 1}
        return JsonResponse(data)

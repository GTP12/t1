import time

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app1.models import *
app_name = 'transaction'
def index(request):


    return render(request,'index.html',locals())

def person_center(request):
    if request.method == 'GET':
        moneys=Moneymanage.objects.filter(user_id=4)
        n=len(moneys)
        totalmoneys=moneys[n-1].mymoney
        myorder=Materialsorder1.objects.filter(user_id=4)
        materialsorder2=Materialsorder2.objects.filter(user_id=4)
        # page_size = 5  # 每页显示5条数据
        # paginator = Paginator(myorder, page_size)
        # try:
        #     golds = paginator.page(page)
        # except :  # 如果用户输入的页码不是整数时，显示第一页
        #     golds = paginator.page(1)
        #

        sellorder1=Sellorder1.objects.filter(user_id=4)
        # page_size = 5  # 每页显示5条数据
        # paginator2 = Paginator(sellorder1, page_size)
        # try:
        #     golds2 = paginator.page(page)
        # except:  # 如果用户输入的页码不是整数时，显示第一页
        #     golds2 = paginator.page(1)
        sellorder2=Sellorder2.objects.filter(user_id=4)
        goldorder1=Goldorder1.objects.filter(user_id=4)
        goldorder2=Goldorder2.objects.filter(user_id=4)
        purchaseorder1=Purchaseorder1.objects.filter(user_id=4)
        purchaseorder2=Purchaseorder2.objects.filter(user_id=4)
    if request.method == 'POST':
            password=str(request.POST.get('password'))
            newpwd1=request.POST.get('newpwd')
            newpwd2=request.POST.get('newpwd2')
            a=User.objects.get(id=4).password
            print(password)
            print(User.objects.get(id=4).password)
            data={}
            if password==str(a) and not newpwd1 and not newpwd2:
                data={
                    'status':'900',
                    'msg':'密码正确'
                }

            elif password and not newpwd1 and not newpwd2:
                data={
                    'status':'901',
                    'msg':'密码不正确请重新输入'
                }
            print(newpwd2,newpwd1)
            if  newpwd1==newpwd2 and newpwd1:
                data = {
                    'status': '200',
                    'ass': '输入正确'
                }
            elif newpwd1 and newpwd2:
                data = {
                    'status': '902',
                    'ass': '两次输入不同'
                }
            if password==str(a) and newpwd1==newpwd2 and newpwd1 :
                data={
                    'status': '201',
                    'sss': '修改密码完成'
                }
                b = User.objects.get(id=4)
                b.password=newpwd1
                b.save()



            return JsonResponse(data)





    return render(request,'center.html',locals())

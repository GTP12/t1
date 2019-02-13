from django.shortcuts import render

from app1.models import Goldorder2, Materialsorder

app_name = 'transaction'


def payment(request, payprice, order_time):
    return render(request, 'pay/payment.html', locals())


def paysuccess(request, order_time):
    goldsorder2 = Goldorder2.objects.get(order_time=order_time)
    goldsorder2.order_state = 0
    goldsorder2.save()
    return render(request, 'pay/paysuccess.html')


def matrialsuccess(request, oreder_time):
    materialsorder2 = Materialsorder.objects.get(oreder_time=oreder_time)
    materialsorder2.order_state = 0
    materialsorder2.save()
    return render(request, 'pay/paysuccess.html', locals())

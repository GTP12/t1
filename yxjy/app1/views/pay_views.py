from django.shortcuts import render

from app1.models import Goldorder2, Materialsorder2

app_name = 'transaction'


def payment(request, payprice, order_time):
    return render(request, 'pay/payment.html', locals())


def paysuccess(request, order_time):
    # userid = request.user
    goldsorder2 = Goldorder2.objects.filter(order_time=order_time)
    materialsorder2 = Materialsorder2.objects.filter(order_time=order_time)
    if goldsorder2:
        goldsorder2[0].order_state = 0
        goldsorder2[0].save()
    elif materialsorder2:
        materialsorder2[0].order_state = 0
        materialsorder2[0].save()
    return render(request, 'pay/paysuccess.html')


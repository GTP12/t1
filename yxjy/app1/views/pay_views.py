from django.shortcuts import render
app_name = 'transaction'

def payment(request):
    pass
    return render(request,'pay/payment.html')

def paysuccess(request):
    pass
    return render(request,'pay/paysuccess.html')
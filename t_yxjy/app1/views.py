from django.shortcuts import render

def may(request):
    return render(request,'index.html')

def go_account_deal(request):
    return render(request,'account-deal.html')

def go_details(request):
    return render(request,'details.html')

def go_account_purchase(request):
    return render(request,'account-purchase.html')


def a_order(request):
    return render(request,'account-order.html')

def p_order(request):
    return render(request,'purchase-order.html')

def pay_code(request):
    return render(request,'pay_code.html')

def go_success(request):
    return render(request,'success.html')

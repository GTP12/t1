from django.shortcuts import render

def may(request):
    return render(request,'index.html')

def go_account_deal(request):
    return render(request,'account-deal.html')

def go_account_purchase(request):
    return render(request,'account-purchase.html')


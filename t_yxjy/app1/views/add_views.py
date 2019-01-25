from django.shortcuts import render
app_name = 'transaction'

def account_deal(request):
    return render(request, 'account/account-deal.html')

def AddCount(request):
    return render(request, 'add/AddCount.html')

def success(request):
    return render(request, 'add/success.html')

def gold_add(request):
    return render(request, 'add/gold_add.html')

def stuff_add(request):
    return render(request, 'add/stuff_add.html')
def Add(request):
    return render(request, 'add/Add.html')
def add_buy(request):
    return render(request, 'add/add_buy.html')
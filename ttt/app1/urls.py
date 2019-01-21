from app1.views import *
from django.urls import path

app_name = 'yxjy'
urlpatterns = [
    path('to/',may),
    path('deal/',go_account_deal,name= 'deal'),
    path('purchase/',go_account_purchase,name= 'pur'),
]

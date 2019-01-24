from app1.views import *
from django.urls import path

app_name = 'yxjy'




urlpatterns = [
    path('to/',may),
    path('deal/',go_account_deal,name= 'deal'),
    path('go_details',go_details,name= 'g_detail'),
    path('purchase/',go_account_purchase,name= 'pur'),
    path('a_order/',a_order,name= 'a_order'),
    path('p_order/',p_order,name= 'p_order'),
    path('p_code/',pay_code,name= 'p_code'),
    path('go_s/',go_success,name= 'g_su'),

]

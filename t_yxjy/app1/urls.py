from app1.views import *
from django.urls import path
urlpatterns = [
    path('index/',index,name='index'),
    path('person_center/',person_center,name='person_center'),


    path('account_deal/',account_deal,name='account_deal'),
    path('account_order/',account_order,name='account_order'),
    path('account_order2/', account_order2, name='account_order2'),
    path('account_purchase/',account_purchase,name='account_purchase'),
    path('details3/',details3,name='details3'),
    path('success_',success_,name='success_'),

    path('AddCount/',AddCount,name='AddCount'),
    path('gold_add/',gold_add,name='gold_add'),
    path('stuff_add/',stuff_add,name='stuff_add'),
    path('Add/',Add,name='Add'),
    path('add_buy/',add_buy,name='add_buy'),
    path('success/',success,name='success'),

    path('gold_deal/',gold_deal,name='gold_deal'),
    path('gold_details/',gold_details,name='gold_details'),
    path('goldPurchase/',goldPurchase,name='goldPurchase'),

    path('login_/',login_,name='login_'),
    path('register/',register,name='register'),

    path('details2/',details2,name='details2'),
    path('material_deal/',material_deal,name='material_deal'),
    path('materialPurchase/',materialPurchase,name='materialPurchase'),

    path('payment/',payment,name='payment'),
    path('paysuccess/',paysuccess,name='paysuccess')
]

from app1.views import *
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('person_center/', person_center, name='person_center'),

    path('account_deal/', account_deal, name='account_deal'),
    path('account_order/', account_order, name='account_order'),
    path('account_order2/', account_order2, name='account_order2'),
    path('account_purchase/', account_purchase, name='account_purchase'),
    path('details3/', details3, name='details3'),
    path('success_', success_, name='success_'),

    path('AddCount/', AddCount, name='AddCount'),
    path('gold_add/', gold_add, name='gold_add'),
    path('stuff_add/', stuff_add, name='stuff_add'),
    path('Add/', Add, name='Add'),
    path('add_buy/', add_buy, name='add_buy'),
    path('success/', success, name='success'),

    # path('gmxy/', ) # 服务协议
    path('gold_deal/<int:area>/<page>/', gold_deal, name='gold_deal'),
    path('gold_default/<int:area>/<page>/', gold_key, name='gold_default'),

    path('gold_details/<int:id>/', gold_details, name='gold_details'),
    path('goldPurchase/<int:id>/', gold_purchase, name='goldPurchase'),
    path('checkphone/', check_phone),  # 验证电话是否正确
    path('checkqq/', check_qq),  # 验证qq号码是否正确
    path('checkmaxprice/', check_maxprice),  # 排序大到小
    path('checkminprice/', check_minprice),  # 排序小到大
    path('checkmaxtime/', check_maxtime),  # 排序大到小
    path('checkmintime/', check_mintime),  # 排序小到大
    path('checkdefault/', check_default),  # 默认排序
    path('checkstock/', check_default),  # 默认排序


    path('login_/', login_, name='login_'),
    path('register/', register, name='register'),
    path('check/', check_username, name='check_username'),
    path('wechat_log/', wechat_log, name='wechat_log'),

    path('details2/<int:id>/', details2, name='details2'),
    path('material_deal/<int:area>/<int:materialid>/<page>/', material_deal, name='material_deal'),
    path('materialPurchase/<int:id>/', material_purchase, name='materialPurchase'),
    path('checknum/', check_num),  # 验证购买数量是否合理

    path('payment/<payprice>/<order_time>', payment, name='payment'),
    path('paysuccess/<order_time>/', paysuccess, name='paysuccess'),
    path('matrialsuccess/<order_time>/', matrialsuccess, name='matrialsuccess')
]

from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from app1.models import User

LOGIN_REQUIRED = ['/games_deal/person_center/','/games_deal/account_deal/','/games_deal/account_purchase/','/games_deal/material_deal/','/games_deal/gold_deal/','/games_deal/Add/']

class LoginMiddleware(MiddlewareMixin):
    def process_request(self,request):  # 接收到请求时
        if request.path in LOGIN_REQUIRED:
            user_id=request.session.get('user_id')
            if user_id: #判断是否登录
                user = User.objects.get(pk=user_id)
                request.user = user
            else:
                return redirect(reverse('transaction:login_'))
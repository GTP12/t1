from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from app1.models import User

LOGIN_REQUIRED_JSON = ['/person_center/,']


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):  # 接收到请求时
        if request.path in LOGIN_REQUIRED_JSON:
            user_id = request.session.get('user_id')
            if user_id:  # 判断是否登录
                user = User.objects.get(pk=user_id)
                request.user = user
            else:
                return redirect(reverse('transaction:login_'))

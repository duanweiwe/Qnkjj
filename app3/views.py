# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


#DEFAULT_FONT['helvetica'] = 'st'


def app3_login(request):
    if request.method == 'GET':
        return render(request, 'app3/app3_login.html', {})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'app3/app3_notice.html')
        else:
            error_message = '用户名或密码错误'
            return render(request, 'app3/app3_login.html', {'error_message': error_message, 'username': username})


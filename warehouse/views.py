from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from warehouse import models

import os

base_dir = "documents"

if not os.path.exists(base_dir):
    os.mkdir(base_dir)


# 登录；
def login(request):
    if request.method == "POST":

        account = request.POST.get('account')
        password = request.POST.get('password')

        # 确保id和password都不为空；
        if account and password:
            account = account.strip()

            # noinspection PyBroadException
            try:
                user = models.User.objects.get(account=account)

                if user.password == password:
                    request.session['account'] = user.account
                    request.session['name'] = user.name
                    request.session['grade'] = user.grade
                    return redirect('/')
                    pass

                else:
                    message = "密码输入不正确！"
            except Exception as e:
                print(e)
                message = "用户名不存在！"

            return render(request, 'warehouse/login.html', {"message": message})

    return render(request, 'warehouse/login.html')


# 注册；
def register(request):
    if request.method == "POST":
        account = request.POST.get('account')
        name = request.POST.get('name')
        password = request.POST.get('password')

        if account and name and password:
            account = account.strip()

            try:
                models.User.objects.get(account=account)
                message = "帐号已存在！"
            except Exception as e:
                print(e)
                models.User.objects.create(account=account, name=name, password=password,
                                           grade=0)
                user = dict()
                user["account"] = account
                user["name"] = name
                return redirect('/')

            return render(request, 'warehouse/register.html', {"message": message})

    return render(request, 'warehouse/register.html')


# 主页；
def index(request):
    if request.session.get("account"):
        user = dict()
        user["account"] = request.session.get("account")
        user["name"] = request.session.get("name")

        file_dir = os.path.join(base_dir, user['account'])
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)

        file_list = os.listdir(file_dir)

        return render(request, 'warehouse/index.html', {"user": user,
                                                        "file_list": file_list})

    else:
        return redirect('/login')

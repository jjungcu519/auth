from django.shortcuts import render, redirect
from .forms import CustomCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
# 장고 내 구현된 기능과 변수의 이름을 다르게 표기해준다.
from django.contrib.auth import logout as auth_logout

def signup(request):
    # 요건 뭐지
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    #get 요청이 들어왔을때    
    else:
        form = CustomCreationForm()
    
    context = {
        'form' : form,
    }
    
    return render(request, 'signup.html', context)

def login(request):
    if request.method =='POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            #경로 2개 -> 정상적 로그인 경로 & 튕겨서 로그인으로 들어오는 경로(next 인자 있음)
            next_url = request.GET.get('next')
            # next 인자에 url 없을때 : None or 'articles:index'
            # next 인자에 url 있을때 : /articles/1/ or 'articles:index'
            return redirect(next_url or 'articles:index')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)

    return redirect('accounts:login')
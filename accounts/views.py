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
            return redirect('articles:index')
    else:
        form = CustomAuthenticationForm()

    context = {
        'form' : form
    }

    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)

    return redirect('accounts:login')
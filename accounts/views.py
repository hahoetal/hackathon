from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/signup.html', {'error' : 'user name is already exist.'})
            else:
                user = User.objects.create_user(
                    username, password=request.POST['password1'])
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')                
        else:
            return render(request, 'accounts/signup.html', {'error' : 'password is incorrect.'})
    return render(request, 'accounts/signup.html')

# def signup(request):
#     if request.method == 'POST':
#         signup_form = SignupForm(request.POST)
#         # 유효성 검증에 통과한 경우 (username의 중복과 password1, 2의 일치 여부)
#         if signup_form.is_valid():
#             # SignupForm의 인스턴스 메서드인 signup() 실행, 유저 생성
#             signup_form.signup()
#             return redirect('post:post_list')
#     else:
#         signup_form = SignupForm()

#     context = {
#         'signup_form': signup_form,
#     }
#     return render(request, 'member/signup.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'home/home.html')
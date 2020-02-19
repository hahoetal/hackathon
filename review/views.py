from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from data.models import Data
from .models import Userreview
from .form import Reviewform

# Create your views here.

def foodinfo(request, data_id): # 음식에 대한 상세 정보를 불러와야 하므로 url을 통해 data_id를 받아온다.(url도 고쳐주기)
    # method가 POST 방식인 경우.
    if request.method == "POST":
        # 리뷰를 작성할 때, 사용자가 메뉴명을 입력하지 않아도 자동으로 입력되도록 하기 위해 넣은 코드.
        data = get_object_or_404(Data, pk=data_id)
        menu_name = data.menu # 가지고 온 객체의 메뉴명을 menu_name에 넣기.
        # 글쓰기
        form = Reviewform(request.POST, request.FILES) # 어떤 형식의 입력 공간에서 입력을 받았는지 알려주고, 입력받은 내용에 어디에 담겨 있는지 알려주기.
        if form.is_valid(): # form이 유효하면
            reviewpost = form.save(commit = False) # 일단 저장하지 말고,
            reviewpost.author = User.objects.get(username = request.user.get_username()) # user 아이디를 받아서 넣고,
            reviewpost.menu = menu_name
            reviewpost.save() # 저장
            return redirect('/review/review/data/'+str(data.pk)) # 페이지 반환
            
    # method가 GET 방식인 경우.
    else:
        # 음식 정보에 대한 세부 사항 불러오기
        data = get_object_or_404(Data, pk=data_id) # pk값을 이용해서 Data 클래스로 만든 특정 객체를 불러오기.
        menu_name = data.menu # 불러온 객체에서 메뉴만 menu_name에 담기.
        form = Reviewform() # 입력받을 폼 띄우기.
        return render(request, 'info.html', {'data':data, 'reviewform':form})

def review(request, data_id):
        data = get_object_or_404(Data, pk=data_id)
        menu_name = data.menu
        # 리뷰가 한 페이지당 세 개씩 보여지게 하기.
        reviews = Userreview.objects.all()
        reviews_list = Userreview.objects.filter(menu__contains=menu_name) # Usearreview 클래스로 만든 모든 객체를 가져와서 그 중 Data객체와 메뉴명이 동일한 리뷰만 가져오고,
        paginator = Paginator(reviews_list, 3) # Paginator를 이용해서 객체들을 원하는 개수 만큼 나누고,
        page = request.GET.get('page') # request된 페이지 번호에 해당하는 페이지를 page에 담고,
        posts = paginator.get_page(page) # request된 페이지를 posts에 담아줌.
        return render(request, 'review_list.html', {'reviews':reviews, 'posts':posts})

# 자기가 작성한 리뷰만 따로 모아서 보게 만들고 싶음....
def myreview(request):
        reviewer = User.objects.get(username = request.user.get_username()) # 현재 로그인한 유저의 아이디를 받아오고,
        myreviews = Userreview.objects.all() # Userreview 클래스로 만든 객체들을 가져오고,
        myreviews_list = Userreview.objects.filter(author = reviewer) # 작성자(author)가 현재 로그인한 유저와 같은 객체만 가져오고,
        paginator = Paginator(myreviews_list, 4) # 로그인한 유저가 쓴 리뷰들을 한 페이지에 네 개씩 오도록 자르고,
        page = request.GET.get('page') # 서버에서 요청 받은 페이지를 받아오고,
        myposts = paginator.get_page(page) # 서버에서 요청 받은 페이지를 받아서 myposts에 넣어서 반환
        return render(request, 'myreviews.html', {'myreviews' : myreviews, 'myposts':myposts})

from django.shortcuts import render, redirect, get_object_or_404
from . import views
from data.models import Data
from .models import Userreview
from .form import Reviewform
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import auth

# Create your views here.

def review(request, data_id): # 음식에 대한 상세 정보를 불러와야 하므로 url을 통해 data_id를 받아온다.(url도 고쳐주기)
    # method가 POST 방식인 경우.
    if request.method == "POST":
        # 음식 정보에 대한 세부 사항 불러오기
        data = get_object_or_404(Data, pk=data_id) # pk값을 이용해서 Data 클래스로 만든 특정 객체를 불러오기.
        # 리뷰를 가지고 오는데 세 개씩 분할해서 가지고 오기.
        reviews = Userreview.objects
        reviews_list = Userreview.objects.all() # Usearreview 클래스로 만든 모든 객체를 가져오고,
        paginator = Paginator(reviews_list, 3) #Paginator 함수를 이용해서, 객체들을 세 개씩 분할하고,
        page = request.GET.get('page') # 분할된 것을 가지고 와서 page(변수)에 넣고???
        posts = paginator.get_page(page) # page가 있으면 가지고 와서 posts에 넣어.
        # 글쓰기
        form = Reviewform(request.POST, request.FILES) # POST 방식으로 들어온 내용과 파일을 Reviewform 클래스에 맞게 담아서 form에 넣기
        if form.is_valid(): # form이 유효하면
            reviewpost = form.save(commit = False) # 일단 저장하지 말고,
            reviewpost.author = User.objects.get(username = request.user.get_username()) # user 아이디를 받아서 넣고,
            reviewpost.save() # 저장
            return redirect('/review/review/data/'+str(data.pk)) # 페이지 반환
    else:
        data = get_object_or_404(Data, pk=data_id)

        reviews = Userreview.objects
        reviews_list = Userreview.objects.all()
        paginator = Paginator(reviews_list, 3)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        form = Reviewform()
        return render(request, 'review.html', {'data':data, 'reviewform':form, 'reviews': reviews, 'posts': posts})



        


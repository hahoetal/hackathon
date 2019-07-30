from django.shortcuts import render, redirect
from . import views
from .models import Userreview
from .form import Reviewform
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import auth

# Create your views here.

# def review(request):
#     reviews = Userreview.objects
#     return render(request, 'review.html', {'reviews': reviews})

def review(request):
    reviews = Userreview.objects
    reviews_list = Userreview.objects.all()
    paginator = Paginator(reviews_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'review.html', {'reviews': reviews, 'posts': posts})


def user_review(request):
    if request.method == "POST":
        form = Reviewform(request.POST, request.FILES)
        if form.is_valid():
            reviewpost = form.save(commit = False)
            reviewpost.author = User.objects.get(username = request.user.get_username())
            reviewpost.save()
            return redirect('review')
    else:
        form = Reviewform()
        return render(request, 'write.html', {'reviewform':form})

        


from django.shortcuts import render, get_object_or_404
from .models import Data

# Create your views here.
def home(request):
    return render(request, 'home.html')

def show(request):
    data = Data.objects
    return render(request, 'show.html', {'data':data})

def sortName(request):
    data = Data.objects.order_by('title')
    return render(request, 'show.html', {'data':data})

def sortPrice(request):
    data = Data.objects.order_by('price')
    return render(request, 'show.html', {'data':data})

def detail(request, data_id):
    data_detail = get_object_or_404(Data, pk=data_id)
    return render(request, 'detail.html', {'data':data_detail})

def search(request):
    try:
        type_search = request.GET.get('selSearchType')
        txt_search = request.GET.get('txtSearch')
        if type_search == "전체":
            search_list = Data.objects.filter(title__contains=txt_search)
            search_list = Data.objects.filter(menu__contains=txt_seaarch)
        elif type_search == "음식점":
            search_list = Data.objects.filter(title__contains=txt_search)
        else:
            search_list = Data.objects.filter(menu__contains=txt_search)
    except:
        search_lists = Data.objects.all()
    return render(request, 'search.html', {'search_list': search_list})


def pricefilter(request):
    try:
 
            minprice = request.GET.get('min_price')
            maxprice = request.GET.get('max_price')
            choice = request.GET.get('category')

            search_list = Data.objects.filter(category__contains= choice).filter(price__gte=minprice).filter(price__lte=maxprice).order_by('price')
           
    except:
            search_list = Data.objects.all()
            search_list = Data.objects.order_by("price")
    return render(request, 'search.html', {'search_list':search_list})

def only__menu(request):
    menu = request.GET.get('food')
    if menu == "전부":
        data = Data.objects.order_by('title')
        return render(request, 'show.html', {'data': data})
    else:
        data = Data.objects.filter(category__contains=menu).order_by('price')
    return render(request, 'show1.html', {'data': data})

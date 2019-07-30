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

# 사용자로부터 음식 종류(1개 혹은 2개 이상)와 가격 범위를 입력받아 메뉴를 필터링해주는 함수.
# 더 간단하게 만들 수 있을 것 같음... 좀 더 고민해보기!!
def pricefilter(request):
    try:
        choice = ['','','','','','']
        search_list = []
        choice_list = []

        minprice = request.GET.get('min_price')
        maxprice = request.GET.get('max_price')

        choice[0] = request.GET.get('category1', 0)
        choice[1] = request.GET.get('category2', 0)
        choice[2] = request.GET.get('category3', 0)
        choice[3] = request.GET.get('category4', 0)
        choice[4] = request.GET.get('category5', 0)
        choice[5] = request.GET.get('category6', 0)
            
        for i in range(0, 6):
            if choice[i] != 0:
                choice_list = Data.objects.filter(category__contains= choice[i]).filter(price__gte=minprice).filter(price__lte=maxprice).order_by("price")
                search_list.extend(choice_list)  # 이게 아주 중요함!!
                # 이 코드를 포함하지 않으면, 가장 나중에 필터링 된 정보만 search_list에 남게 됨.
                # 리스트명1.extend(리스트명2)은 리스트1에 리스트2의 내용을 포함시켜줌.
        return render(request, 'search.html', {'search_list':search_list})
                    
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

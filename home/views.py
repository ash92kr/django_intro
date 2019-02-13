from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):   # 장고에서는 뷰 함수의 인자에 항상 request를 넣어야 한다
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django!')

def dinner(request):
    
    menus = ['치킨돈부리', '라면', '맘스터치 싸이버거', '빵']
    pick = random.choice(menus)

    # return HttpResponse(one)
    return render(request, 'dinner.html', {'menus': menus, 'pick': pick})


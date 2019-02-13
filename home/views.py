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


def hello(request, name):
    return render(request, 'hello.html', {'name': name})


def cube(request, num):
    num3 = int(num) ** 3
    return render(request, 'cube.html', {'num': num, 'num3': num3})


def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')   # 딕셔너리로 값을 보내고 받음
    return render(request, 'pong.html', {'data': data})
    
    
def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'nickname': nickname, 'pwd': pwd})
    
    
    
    
    
    
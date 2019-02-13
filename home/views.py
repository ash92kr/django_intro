from django.shortcuts import render, HttpResponse
from pprint import pprint

# Create your views here.
def index(request):   # 장고에서는 뷰 함수의 인자에 항상 request를 넣어야 한다
    print(request)
    print(type(request))
    pprint(request.META)
    return HttpResponse('Welcome to Django!')




from django.urls import path
from . import views   # 자신의 폴더에 있는 views를 부름

urlpatterns = [
    path('', views.index, name='index'),   # url 주소는 /utilities이고 뒤에 아무 것도 안 붙음
    ]




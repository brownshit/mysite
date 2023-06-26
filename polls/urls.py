from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name='index'),
    #127.0.0.1/polls/ 라는 url이 들어오게 되면, path구문으로 polls를 잡아낸다
    #그럼 이 파일로 이동해서 views.Index로 이동한다.
]

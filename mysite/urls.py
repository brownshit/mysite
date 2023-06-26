"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#여기서 요청한 주소를 잘게 쪼개어 주는 역할을 한다. pathing 이라고 한다.

#여기가 최상위 urlconf이다.
#여기서 url을 pathing 하고 받아서 하위 앱의 url로 연결해준다.
from django.contrib import admin
from django.urls import include,path
#include함수는 다른 urconf들을 참조할 수 있도록 도와준다.
urlpatterns = [
    path('polls/',include('polls.urls')),
    #127.0.0.1/polls/ 라는 url이 들어오게 되면, path구문으로 polls를 잡아낸다
    path('admin/', admin.site.urls),
]

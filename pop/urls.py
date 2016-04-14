"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please s
ee:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, in
clude
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^catagory_list/$',catagory_list,name='catagory_list'),
    url(r'^catagory/$',catagory,name='catagory'),
    url(r'^catagory/item/$',item,name='item'),
    url(r'^catagory/item/detail/$',detail,name='detail'),
]


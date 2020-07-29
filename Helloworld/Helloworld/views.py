
from django.http import HttpResponse
from django.shortcuts import  render
from datetime import datetime


def master(request):
    return render(request, 'master.html')


def hello1(request):
    # return HttpResponse("Hello World!")
    title_dict = {"one": '你好', 'two': "你不好"}
    a_list = []
    f1 = 'abcde bb cc dd ee ff',
    re_dict = {'title': title_dict,
               'f1': f1,
               'timez': datetime.now(),
               'num': 1024,
               'zero': 0,
               "a_list": a_list,
               }
    #  body views_str all_dict
    return render(request, 'hello1.html', re_dict)


def hello2(request):
    # return HttpResponse("Hello World!")
    title_dict = {"one": '你好', 'two': "你不好"}
    body_list = ["welcome", 'to']
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    all_dict = [{"name": "name1"}, {"name": "name2"}, {"name": "name3"}]
    re_dict = {
               'title': title_dict,
               'body': body_list,
               'views_str': views_str,
               'all_dict': all_dict,
               }
    #  f1 num a_list timez  zero
    return render(request, 'hello2.html', re_dict)


def form1(request):
    return  render(request,'form.html')


def my_filter(request):
    return render(request, 'my_filter.html')
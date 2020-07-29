from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse


# 表单
def search_form(request):
    return render(request, 'search_form.html', {'method': "get"})


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    print(request.GET)
    if 'qqq' in request.GET and request.GET['qqq']:
        message = '你搜索的内容为: ' + request.GET['qqq']
    else:
        message = '你提交了空表单'
    return HttpResponse('<p>'+message+'</p>'+'<p>'+str(request.GET)+'</p>')


def search_p(request):
    return render(request, 'search_p.html', {'method': "post"})


# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['qqq']
    ctx['method'] = 'post'
    print(request.POST)
    ctx['content'] = request.POST
    return render(request, "search_post.html", ctx)


def get_request(request):
    message = request.method + ' ' + request.path
    return HttpResponse(message)


def redir(request):
    """重定向"""
    # return redirect('/search_form')
    # 方向解析地址
    return redirect(reverse('search_post'))

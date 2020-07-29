from django.shortcuts import render

# Create your views here.

app_name = 'mytag'


def my_tag(request):
    return render(request, 'my_filter.html',{'name': "23456u"})
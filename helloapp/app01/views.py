from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from . import models

app_name = 'app01'


def add_book(request):
    book = models.Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    # books = models.Book.objects.create(title="如来神掌", \
    # price=200, publish="功夫出版社", pub_date="2010-10-10")
    book.save()
    return HttpResponse("<p>数据添加成功！</p>")


def get_book(request):
    books = models.Book.objects.filter(pk=5)
    # books = models.Book.objects.get(pk=5)  # 只获取条件中的一个
    # books = models.Book.objects.all()
    # books = models.Book.objects.exclude(pk=5) # exclude 查询不符合条件的数据
    # books = models.Book.objects.order_by("-price")  # 查询所有，按照价格降序排列
    # books = models.Book.objects.order_by("-price").reverse() # 降序再反转
    # books = models.Book.objects.count() # 查询所有数据的数量
    # books = models.Book.objects.first()  # 返回所有数据的第一条数据
    # books = models.Book.objects.last()  # 返回所有数据的最后一条数据
    # 判断是否有数据，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
    #  books = models.Book.objects.first().exists()
    # books = models.Book.objects.values("pk", "price")  # 查询所有的id字段和price字段的数据
    # 查询所有的price字段和publish字段的数据
    # books = models.Book.objects.values_list("price", "publish")
    # books = models.Book.objects.values_list("publish").distinct()
    # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
    # books = models.Book.objects.distinct()
    # 查询价格为200或者300的数据
    # books = models.Book.objects.filter(price__in=[200, 300])
    # __gt 大于号、__gte 大于等于、__lt 小于、__lte 小于等于、
    # __range 在 ... 之间，左闭右闭区间，__contains 包含
    # __icontains 不区分大小写的包含
    # __startswith 以指定字符开头
    # __endswith 以指定字符结尾
    # __year 是 DateField 数据类型的年份
    # __month 是DateField 数据类型的月份
    # __day 是DateField 数据类型的天数
    print(books)
    print("//////////////////////////////////////")
    books = models.Book.objects.filter(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    return HttpResponse("<p>查找成功！{}</p>".format(books[0].titile))
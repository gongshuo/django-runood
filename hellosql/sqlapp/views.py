from django.shortcuts import render,HttpResponse
from . import  models

# Create your views here.


def add_book(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    print(book, type(book))
    return  HttpResponse('<p>插入数据成功</p>')


def add_book2(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(id=1).first()
    #  获取出版社对象的id
    pk = pub_obj.id
    #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
    print(book, type(book))
    return HttpResponse('<p>插入数据成功</p>')


def add_book3(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book.objects.filter(title="菜鸟教程").first()
    print(book.title)
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    book.authors.add(chong, ying)
    # sqlapp_book_authors 表增加两条记录
    print(book.title)
    return HttpResponse('<p>插入数据成功</p>')


def add_book4(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    #  获取作者对象的id
    pk = chong.pk
    #  获取书籍对象
    book = models.Book.objects.filter(title="冲灵剑法").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象的id
    book.authors.add(pk)
    # sqlapp_book_authors 表增加一条记录
    print(book.title)
    return HttpResponse('<p>插入数据成功</p>')


def add_book5(object):
    book_obj = models.Book.objects.get(id=1)
    author_list = models.Author.objects.filter(id__gt=2)
    book_obj.authors.add(*author_list)  # 将 id 大于2的作者对象添加到这本书的作者集合中
    # 方式二：传对象 id
    book_obj.authors.add(*[1, 3])  # 将 id=1 和 id=3 的作者对象添加到这本书的作者集合中


def add_book5(object):
    ying = models.Author.objects.filter(name="任盈盈").first()
    book = models.Book.objects.filter(title="冲灵剑法").first()
    # 反向：小写表名_set
    ying.book_set.add(book)


def add_book6(object):
    # create()：创建一个新的对象，并同时将它添加到关联对象集之中。
    pub = models.Publish.objects.filter(name="明教出版社").first()
    wo = models.Author.objects.filter(name="任我行").first()
    book = wo.book_set.create(title="吸星大法", price=300,
                              pub_date="1999-9-19", publish=pub)
    print(book, type(book))


def add_book7(object):
    # remove()：从关联对象集中移除执行的模型对象。
    author_obj = models.Author.objects.get(id=1)
    book_obj = models.Book.objects.get(id=11)
    author_obj.book_set.remove(book_obj)


def add_book8(object):
    # clear()：从关联对象集中移除一切对象，删除关联，不会删除对象。
    # 对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在。
    # 无返回值
    #  清空独孤九剑关联的所有作者
    book = models.Book.objects.filter(title="菜鸟教程").first()
    book.authors.clear()


def find_data1(object):
    # 一对多
    # 查询主键为1的书籍的出版社所在的城市（正向）。
    book = models.Book.objects.filter(id=1).first()
    res = book.publish.city
    print(res, type(res))


def find_data2(object):
    # 一对多
    # 反向：对象.小写类名_set(pub.book_set) 可以跳转到关联的表(书籍表)。
    # pub.book_set.all()：取出书籍表的所有书籍对象，在一个 QuerySet 里，遍历取出一个个书籍对象。
    pub = models.Publish.objects.filter(name="明教出版社").first()
    res = pub.book_set.all()
    for i in res:
        print(i.title)


def find_data3(object):
    # 一对一
    # 查询令狐冲的电话（正向）
    # 正向：对象.属性 (author.au_detail) 可以跳转到关联的表(作者详情表)
    author = models.Author.objects.filter(name="令狐冲").first()
    res = author.au_detail.tel
    print(res, type(res))


def find_data4(object):
    # 一对一的反向，用 对象.小写类名 即可，不用加 _set。
    # 反向：对象.小写类名(addr.author)可以跳转到关联的表(作者表)。
    addr = models.AuthorDetail.objects.filter(addr="黑木崖").first()
    res = addr.author.name
    print(res, type(res))


def find_data5(object):
    # 多对多
    # 正向：对象.属性(book.authors)可以跳转到关联的表(作者表)。
    book = models.Book.objects.filter(title="菜鸟教程").first()
    res = book.authors.all()
    for i in res:
        print(i.name, i.au_detail.tel)


def find_data6(object):
    # 多对多
    # 查询任我行出过的所有书籍的名字（反向）。
    author = models.Author.objects.filter(name="任我行").first()
    res = author.book_set.all()
    for i in res:
        print(i.title)


def find_data7(object):
    # 一对多 跨表查询
    # 正向：属性名称__跨表的属性名称 反向：小写类名__跨表的属性名称
    res = models.Book.objects.filter(publish__name="菜鸟出版社").values_list("title", "price")


def find_data8(object):
    # 一对多 跨表查询
    # 反向：通过 小写类名__跨表的属性名称（book__title，book__price） 跨表获取数据
    res = models.Publish.objects.filter(name="菜鸟出版社").values_list("book__title", "book__price")


def find_data9(object):
    # 多对多 跨表查询
    # 正向：通过属性名称__跨表的属性名称(authors__name)跨表获取数据：
    res = models.Book.objects.filter(authors__name="任我行").values_list("title")
    # 反向：通过小写类名__跨表的属性名称（book__title） 跨表获取数据：
    res2 = models.Author.objects.filter(name="任我行").values_list("book__title")


def find_data10(object):
    # 一对一 跨表查询
    # 正向：通过 属性名称__跨表的属性名称(au_detail__tel) 跨表获取数据。
    res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")


def find_data11(object):
    # 一对一 跨表查询
    # 反向：通过 小写类名__跨表的属性名称（author__name） 跨表获取数据。
    # Author对象有一个au_detail_id 指向AuthorDetail
    res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")


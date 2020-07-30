from django.db import models

# Create your models here.
# 表结构
# 书籍表 Book：title 、 price 、 pub_date 、 publish（外键，多对一） 、 authors（多对多）
# 出版社表 Publish：name 、 city 、 email
# 作者表 Author：name 、 age 、 au_detail（一对一）
# 作者详情表 AuthorDetail：gender 、 tel 、 addr 、 birthday


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    # models.ForeignKey("关联类名", on_delete=models.CASCADE)。
    authors = models.ManyToManyField("Author")
    # book 和 author 表关联表


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)
    #   OneToOneField = ForeignKey(...，unique=True)设置一对一。


class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
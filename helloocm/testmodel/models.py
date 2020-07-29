from django.db import models

# Create your models here.
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    degree = models.CharField(choices=(('cj', u'初级'),
                                       ('zj', u'中级'),
                                       ('gj', u'高级')),
                              max_length=2, verbose_name=u'难度')
    # 第一个参数是真正的model参数，#第二个参数则是方便人们理解阅读
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )


class Tag(models.Model):
    contact = models.ForeignKey(Test, on_delete=models.CASCADE,)
    name  = models.CharField(max_length=50)
    dispict = models.TextField()

    # class Meta:
        # abstract = True
        # db_table = ""

    def __unicode__(self):
        return self.name
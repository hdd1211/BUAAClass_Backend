from django.db import models


# Create your models here.
# def class Course

class User_account(models.Model):
    # add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    name = models.CharField(max_length=20, verbose_name='用户名', primary_key=True)
    password = models.CharField(max_length=20, verbose_name="密码")
    # build_time = models.DateTimeField(auto_now_add=add_time, verbose_name='账号创建时间')
    user_photo = models.ImageField(verbose_name='用户头像')


class Evaluation(models.Model):
    # time = models.DateTimeField(auto_now_add=time, verbose_name='评价生成时间')
    user = models.CharField(max_length=20, verbose_name='评价用户')
    comment = models.CharField(max_length=500, verbose_name='评价内容')
    # eva_course


class College(models.Model):
    name = models.CharField


#    courses


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name='教师姓名', primary_key=True)
    # courses = models.ManyToManyField(Course)
    photo = models.ImageField(verbose_name='教师图片')


class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name='教师姓名', primary_key=True)
    credit = models.FloatField(verbose_name='学分', editable=False)
    teacher = models.ManyToManyField(Teacher)
    # 此处不需要再有一个teacher属性？或是teacher中不需要course属性？(MTMF类型会提供反向调用的参数)

    # testtststsdsds

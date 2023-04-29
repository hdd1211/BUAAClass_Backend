import datetime

from django.db import models


# Create your models here.
# def class Course

class User(models.Model):
    id = models.IntegerField(verbose_name='用户ID', auto_created=True, primary_key=True)
    name = models.CharField(verbose_name='用户ID', max_length=20, null=False)
    password = models.CharField(verbose_name="密码", max_length=20, null=False)
    time = models.DateTimeField(verbose_name='账号创建时间', auto_now_add=datetime.datetime.now())
    # user_photo = models.ImageField(verbose_name='用户头像')


class Admin(models.Model):
    id = models.IntegerField(verbose_name='管理员ID', auto_created=True, primary_key=True)
    username = models.CharField(verbose_name='管理员名', unique=True, null=False)
    password = models.CharField(verbose_name='管理员密码', null=False)


class Evaluation(models.Model):
    evaluationid = models.IntegerField(verbose_name='评价ID', primary_key=True, auto_created=True)
    userid = models.IntegerField(verbose_name='评价用户ID')
    content = models.CharField(verbose_name='评论内容', max_length=500)
    likenum = models.IntegerField(verbose_name='赞数量')
    dislikenum = models.IntegerField(verbose_name='踩数量')

    time = models.DateTimeField(verbose_name='评价生成时间', auto_now_add=datetime.datetime.now())

    # eva_course


class College(models.Model):
    name = models.CharField(verbose_name='学院名')
    num = models.IntegerField(verbose_name='学院名系号')
    courses = models.ManyToManyField(Course)


#    courses


class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name='教师姓名', primary_key=True)
    # courses = models.ManyToManyField(Course)
    photo = models.ImageField(verbose_name='教师图片')
    info_url = models.URLField(verbose_name='教师资料链接')


class Course(models.Model):
    id = models.IntegerField(verbose_name='课程ID', primary_key=True, unique=True, auto_created=True)
    name = models.CharField(verbose_name='课程名', max_length=20, null=False, unique=True)
    teacher = models.CharField(verbose_name='教师名', max_length=20, null=False, unique=True)
    Introduction = models.CharField(verbose_name='教师简介', null=False, unique=True)
    Semester = models.IntegerField(verbose_name='课程学期', null=False, unique=True)
    evaluation = models.IntegerField(verbose_name='评分', null=False, unique=True)
    quality = models.IntegerField(verbose_name='内容评分', null=False, unique=True)
    workload = models.IntegerField(verbose_name='工作量评分', null=False, unique=True)
    appraisal = models.IntegerField(verbose_name='考核评分', null=False, unique=True)


class report(models.Model):
    reportid = models.IntegerField(verbose_name='举报ID', primary_key=True)
    userid = models.IntegerField(verbose_name='用户ID')
    index = models.indexes()
    content = models.CharField(verbose_name='反馈内容')

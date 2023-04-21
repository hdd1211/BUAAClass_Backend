from django.db import models


# Create your models here.

class User(models.Model):
    # add_time = models.DateTimeField(default=datetime.now(), verbose_name="添加时间")

    user_name = models.CharField(max_length=20, verbose_name='用户名', primary_key=True)
    password = models.CharField(max_length=20, verbose_name="密码")
    # user_signup_time = models.DateTimeField(auto_now_add=time, verbose_name='账号创建时间')
    # user_photo = models.ImageField

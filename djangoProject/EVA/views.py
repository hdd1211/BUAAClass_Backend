# Create your views here.
from django.http import HttpResponse

from models import User_account


def index(request):
    return HttpResponse("Hello, world. You're at the eva index.")


def add_user(user_name, password):
    if (User_account.objects.filter(user_name=user_name).exists()):
        return 1
    else:
        user = User_account.objects.create(name=user_name, password=password)
        user.save()
        return 0


def delete_user(user_name):
    if (User_account.objects.filter(user_name=user_name).exists()):
        user = User_account.objects.get(user_name=user_name)
        user.delete()
        return 0
    else:
        return 1


def get_user_needmodify(user_name):
    if (User_account.objects.filter(user_name=user_name).exists()):
        user = User_account.objects.get(user_name=user_name)
        return user
    else:
        return 1


def modify_password(user_name, password):
    if (User_account.objects.filter(user_name=user_name).exists()):
        user = User_account.objects.get(user_name=user_name)
        user.password = password
        return 0
    else:
        return 1


def check_password(user_name, password):
    user = User_account.objects.get(user_name=user_name)
    if (password == user.password):
        return 0
    else:
        return 1

# def check_user()

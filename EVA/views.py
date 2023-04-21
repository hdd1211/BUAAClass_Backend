# Create your views here.
from django.http import HttpResponse

from models import User


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def add_user(user_name, password):
    if (User.objects.filter(user_name=user_name).exists()):
        return False
    else:
        user = User.objects.create(name=user_name, password=password)
        user.save()
        return True


def delete_user(user_name):
    if (User.objects.filter(user_name=user_name).exists()):
        user = User.objects.get(user_name=user_name)
        user.delete()
        return True
    else:
        return False


def get_user_needmodify(user_name):
    if (User.objects.filter(user_name=user_name).exists()):
        user = User.objects.get(user_name=user_name)
        return user
    else:
        return False


def modify_password(user_name, password):
    if (User.objects.filter(user_name=user_name).exists()):
        user = User.objects.get(user_name=user_name)
        user.password = password
        return True
    else:
        return False


def check_password(user_name, password):
    user = User.objects.get(user_name=user_name)
    if (password == user.password):
        return True
    else:
        return False

# def check_user()

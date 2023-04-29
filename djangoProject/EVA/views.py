# Create your views here.
from django.http import HttpResponse, JsonResponse

from .models import User


# def


def index(request):
    return HttpResponse("Hello, world. You're at the eva index.")


# user part:
def add_user(request):
    user_name = request.POST.get('user_name')
    if (User.objects.filter(user_name=user_name).exists()):
        response_data = {'success': 1, 'message': '账号已存在'}
        return JsonResponse(response_data)
    else:
        user = User.objects.create(name=user_name, password=password)
        user.save()
        response_data = {'success': 0, 'message': '成功注册'}
        return JsonResponse(response_data)


def delete_user(request):
    user_name = request.POST.get('user_name')
    if (User.objects.filter(user_name=user_name).exists()):
        user = User.objects.get(user_name=user_name)
        user.delete()
        response_data = {'success': 0, 'message': '成功注销'}
        return JsonResponse(response_data)
    else:
        response_data = {'success': 1, 'message': '账号不存在'}
        return JsonResponse(response_data)


def get_user_needmodify(request):
    user_name = request.POST.get('user_name')
    if (User.objects.filter(user_name=user_name).exists()):
        user = User.objects.get(user_name=user_name)

        return user
    else:
        return 1


def modify_password(request):
    user_name = request.POST.get('user_name')
    new_password = request.POST.get('new_password')
    if (User.objects.filter(user_name=user_name).exists()):
        user = User.objects.get(user_name=user_name)
        user.password = new_password
        response_data = {'success': 0, 'message': '成功修改密码'}
        return JsonResponse(response_data)
    else:
        response_data = {'success': 1, 'message': '未找到用户'}
        return JsonResponse(response_data)


def check_password(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        if User.objects.filter(user_name=user_name):
            if User.objects.filter(password=password):
                response_data = {'success': 1, 'message': '用户名和密码未匹配成功'}
                return JsonResponse(response_data)
            else:
                response_data = {'success': 0, 'message': '用户名和密码匹配成功'}
                return JsonResponse(response_data)
        else:
            response_data = {'success': 2, 'message': '用户未注册'}
            return JsonResponse(response_data)


# def check_user()


# college:

# Course:
def add_course(request):
    name = request.POST.get('course_name')

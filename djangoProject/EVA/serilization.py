from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, Course, Evaluation, Teacher, Admin, Report, Announcement
import json


class Response(res):

    def get_response(self, res):
        if res == 0:
            return 0
        elif res == 1:
            return 1
        elif res == 2:
            return 2


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'agree_reviews', 'disagree_reviews', 'reviews']

    def get_user(self, user):
        model = User
        fields = '__all__'
        # data = [user.id, user.name, user.password, user.agree_reviews, user.disagree_reviews, user.reviews]
        return data


class LoginSerializer(serializers.Serializer):
    res = Response()
    user = UserSerializer()

    class Meta:
        field = ['res', 'user']

    def get_login(self, res, user):
        data = [Response.get_response(res), UserSerializer.get_user(user)]
        return data


class RegisterSerializer(serializers.Serializer):
    res = Response()

    class Meta:
        field = ['res']

    def get_register(self, res):
        data = [Response.get_response(res)]
        return data


class InteractionsSerializer(serializers.Serializer):
    res = Response()

    class Meta:
        field = ['res', 'value']

    def get_interaction(self, res, value):
        data = [Response.get_response(res), value]
        return data


class CourselistSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'
        # field = ['id', 'name', 'department', 'credit',
        #          'semester', 'rating_total', 'rating_quality',
        #          'rating_workload', 'rating_appraisal', 'review_ids',
        #          'teacher', 'Introduction', 'evaluation', 'teacher']

    def get_courselist(self):
        courses = Course.objects.all()
        for course in courses:
            data = [course.id, course.name, course.department, course.credit,
                    course.semester, course.rating_total, course.rating_quality,
                    course.rating_workload, course.rating_appraisal,
                    course.review_ids, course.teacher, course.Introduction,
                    course.evaluation, course.teacher]
        return data


class EvaluationSerilizer(serializers.Serializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

    def get_evaluation(self, id):
        evaluation = Evaluation.objects.get(id=id)
        serializer = EvaluationSerilizer(evaluation)
        data = serializer.data
        return data


class AnnouncementSerilizer(serializers.Serializer):
    class Meta:
        model = Announcement
        fields = '__all__'

    def get_announcement(self):
        announcement = Announcement.objects.last()
        serializer = AnnouncementSerilizer(announcement)
        data = serializer.data
        return data


class AdminLoginSerializer(serializers.Serializer):
    class Meta:
        model = Admin
        fields = '__all__'

    def get_admin(self, admin):
        serializer = AdminLoginSerializer(admin)
        data = serializer.data
        return data


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'

    def get_course(self, course):
        serializer = CourseSerializer(course)
        data = serializer.data
        return data


class DelcourseSerializer(serializers.Serializer):
    class Meta:
        field = ['res']

    def get_delcourse(self, res):
        data = [Response.get_response(res)]
        return data

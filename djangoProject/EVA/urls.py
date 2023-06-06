from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('api/admin_catalog_get_by_id/', views.get_by_id, name='get_course_byid'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/course_list/', views.course_list, name='course_list'),
    path('api/wordcloud', views.wordcloud, name='wordcloud'),
    path('api/login', views.login, name='login'),
    path('api/register', views.register, name='register'),
    path('api/review', views.login, name='review'),
    path('api/release', views.release, name='release'),
    path('api/interaction', views.interaction, name='interaction'),
    path('api/report', views.report, name='report'),
    path('api/concerning', views.concerning, name='concerning'),
    path('api/recommend', views.recommend, name='recommend'),
    path('api/announcement', views.announcement, name='announcement'),
    path('api/admin_login', views.admin_login, name='admin_login'),
    path('api/admin_catalog_all', views.admin_catalog_all, name='admin_catalog_all'),
    path('api/admin/review/get_by_status/<int:status>', views.get_reviews_by_status),
    path('api/admin/review/get_by_user/<str:user_id>', views.get_reviews_by_user),
    path('api/admin/review/get_by_course/<str:course_id>', views.get_reviews_by_course),
    path('api/admin/review/get_by_word/<str:word>', views.get_reviews_by_word),
    path('api/admin/review/del_review/<str:id>', views.del_review),
    path('api/admin/review/del_batch', views.del_batch),
    path('api/admin/review/get_by_id', views.get_review_by_id),
    # path('api/admin_catalog_get_by_id/', views.get_by_id, name='get_course_byid'),
]

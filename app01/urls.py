from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('task01/', task_01),  # http://127.0.0.1:8000/app01/task01/
    path('task02/', task_02),  # http://127.0.0.1:8000/app01/task02/
    path('task03/<int:cat_id>/', task_03),  # http://127.0.0.1:8000/app01/task03/123/
    path('task04/<slug:cat>/', task_04),  # http://127.0.0.1:8000/app01/task04/123qwe/
    re_path(r'^task05/(?P<year>[0-9]{4})/', task_05),  # http://127.0.0.1:8000/app01/task05/2020/
    path('task06/', task_06),  # http://127.0.0.1:8000/app01/task06/?name=Gagarina&type=pop
    re_path(r'^task07/(?P<year>[0-9]{4})/', task_07),  # http://127.0.0.1:8000/app01/task07/2024/
    re_path(r'^task08/(?P<year>[0-9]{4})/', task_08),  # http://127.0.0.1:8000/app01/task08/2024/
    re_path(r'^task09/(?P<year>[0-9]{4})/', task_09),  # http://127.0.0.1:8000/app01/task09/2024/
    re_path(r'^task10/(?P<year>[0-9]{4})/', task_10),  # http://127.0.0.1:8000/app01/task10/2024/

    # path('', index, name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),  # http://127.0.0.1:8000/about/
    # path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    # path('post/<int:post_id>/', show_post, name='post'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    # path('category/<slug:cat_slug>/', show_category, name='category'),

    path('', WomenHome.as_view(), name='home'),  # http://127.0.0.1:8000/
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('addpage/', AddPage.as_view(), name='add_page'),

]


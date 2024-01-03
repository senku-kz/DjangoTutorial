"""
URL configuration for djangoProjectTutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app01.views import page_not_found
from djangoProjectTutorial import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app01.urls')),  # http://127.0.0.1:8000/app01/task01/
    # path('app01/task01/', app01.views.task_01),  # http://127.0.0.1:8000/app01/task01/
    # path('app01/task02/', app01.views.task_02),  # http://127.0.0.1:8000/app01/task02/
]

handler404 = page_not_found  # http://127.0.0.1:8000/app01/page_not_found/

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""awuyanjundada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from bfirst_step.views import *
from bfirst_step import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('batch/',include('bfirst_step.yemian_urls')),
    path('<int:id>/details/',views.details),
    path('fenyessd/<int:id>/',views.fenyessd),
    path('<int:id>/delete/',views.delete_details_listnames)
    # path('', index),
    # path('index_id/<index_id>/<index_name>', views.index_id ),
]

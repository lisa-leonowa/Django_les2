"""
URL configuration for DjangoLess2 project.

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
from django.contrib import admin
from django.urls import path
from Lesson2 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.read_client),
    path('clients', views.read_client),
    path('clients/create', views.create_client),
    path('clients/<int:id>/', views.client_detail_view),

    path('goods', views.read_good),
    path('goods/create', views.create_good),
    path('goods/update/<int:id>/', views.update_good),

    path('orders', views.read_order),
    path('orders/create', views.create_order),
    path('orders/delete/<int:id>/', views.delete_order),
]
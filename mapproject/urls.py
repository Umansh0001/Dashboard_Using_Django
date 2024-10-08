"""mapproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from map import views as map_views  # Import all views from map

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_views.pincode_search, name='index'),
    path('upload/', map_views.upload_file, name='upload_file'),
    path('success/', map_views.success, name='success'),
    path('pincode_search/', map_views.pincode_search, name='pincode_search'),
    path('clear_data/', map_views.clear_data, name='clear_data'),  # Import clear_data view
]


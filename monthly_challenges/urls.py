"""
URL configuration for monthly_challenges project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# This is the entire project URL page that starts with different paths for different apps in the project
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("challenges/", include("challenges.urls")) ##### Core Concept of Django:
    # An app called challenges. all requests start with /challenges of the domain would be inquote forward to challenges app,
    # then check the URL config there and see what comes after /challenges, (Ex. january) and look for january in the URL config and find which veiw function should be called
]

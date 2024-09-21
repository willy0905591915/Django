from django.urls import path
from . import views

# this create a URL config
urlpatterns = [
    path("<month>", views.monthly_challenges)
]
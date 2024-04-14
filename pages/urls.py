from django.urls import path
from .views import HomeView, classifier


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("result/", classifier, name="result"),
]

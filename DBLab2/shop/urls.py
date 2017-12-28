from django.conf.urls import url, include
from shop import views

urlpatterns = [
    url(r"^delete", views.Delete.as_view(), name="Delete"),
    url(r"^create", views.Create.as_view(), name="Create"),
    url(r"^$", views.Home.as_view(), name="Home"),
]
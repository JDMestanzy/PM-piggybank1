from django.urls import path
from .views import indexPageView
from .views import accountPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("account/<kidName>", accountPageView, name="account")
]

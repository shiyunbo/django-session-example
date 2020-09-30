from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('verify', views.code_verify, name="code_verify"),
]

from django.urls import path
from gate import views


urlpatterns = [
    path(r"", views.index),
    path(r"open", views.open),
    path(r"rfid", views.rfid),
]

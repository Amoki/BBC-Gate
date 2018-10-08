from django.urls import path
from gate import views


urlpatterns = [path(r"open", views.open), path(r"", views.index)]

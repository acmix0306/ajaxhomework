# from django.contrib import admin
from django.urls import path
from . import views #加入此句匯入home/view

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('',views.index),
]
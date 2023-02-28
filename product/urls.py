from django.contrib import admin
from django.urls import path, include
from product.views import *


urlpatterns = [
    path('api/sneakers', ProductView.as_view()),
    path('api/sneakers/<int:pk>/', ProductDetail.as_view())
]
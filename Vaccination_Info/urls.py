from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('pdf_view/', views.ViewPDF),
    path('pdf_download/', views.DownloadPDF),
]

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.import_data_to_db, name="home"),
    path(
        "export_data_to_excel", views.export_data_to_excel, name="export_data_to_excel"
    ),
]

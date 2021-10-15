from django.urls import path
from . import views

urlpatterns = [
    path(r'list/', list_directory),
    path(r'list/<path:path>', list_directory),
    path(r'download/directory/<path:path>', download_directory),
    path(r'download/file/<path:path>', download_file),
    path(r'add/file/<path:path>', add_file),
    path(r'view/<path:path>', view_file),
]

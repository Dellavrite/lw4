from django.urls import include, path
from .views import *

urlpatterns = [
    path('', view_film),
    path('add/', create_film),
    path('edit/<int:pk>', edit_film),
    path('delete/<int:pk>', delete_film),
]
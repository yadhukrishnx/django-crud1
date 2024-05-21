from django.urls import path
from . import views

urlpatterns = [
    path("",views.createbook),
    path("detailedview/<int:book_id>/",views.detailedview),
]
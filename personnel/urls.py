from django.urls import path
from .views import (DepartmentListCreateView,
                    DepartmentRUDView,
                    PersonnelListCreateView,
                    PersonnelRUDView)


urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view()),
    path('departments/<str:pk>/', DepartmentRUDView.as_view()),
    path('personnels/',  PersonnelListCreateView.as_view()),
    path('personnels/<str:pk>/', PersonnelRUDView.as_view()),
]

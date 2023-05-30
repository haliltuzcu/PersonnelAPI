from django.urls import path, include
from .views import RagesterView


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RagesterView.as_view()),
]

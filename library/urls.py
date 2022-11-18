from django.urls import path

from library import views


urlpatterns = [
    path ( '<pk>/', views.InfoViews.as_view () ),
]

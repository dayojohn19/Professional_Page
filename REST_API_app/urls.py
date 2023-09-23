from django.urls import path
from . import views


app_name = "REST_API_app"

urlpatterns = [
    path('',views.defaultRoutes),
]

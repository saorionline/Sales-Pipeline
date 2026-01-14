from django.urls import path
from . import views

urlpatterns = [
    path('webhooks/pandadoc/', views.pandadoc_webhook, name='pandadoc_webhook'),
]
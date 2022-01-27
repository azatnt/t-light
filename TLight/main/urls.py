from django.urls import path
from .views import *


urlpatterns = [
    path('clients', Clients.as_view(), name='clients_urls'),
    path('legal_entity', LegalEntity.as_view(), name='legal_entity_urls'),
    path('department', Department.as_view(), name='department_urls')
]
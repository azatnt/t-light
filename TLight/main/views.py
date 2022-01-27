from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Prefetch




class Clients(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        clients = TClient.objects.all().select_related('id_status', 'mail', 'gender').order_by('id')
        result_page = paginator.paginate_queryset(clients, request)
        data = ClientSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)


class LegalEntity(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        legal_entity = TLegalEntity.objects.filter().prefetch_related(
            Prefetch('legal_dept', queryset=TLegalEntityDepartment.objects.filter().select_related('id_department')))
        result_page = paginator.paginate_queryset(legal_entity, request)
        data = LegalEntitySerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)


class Department(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        legal_entity = TDepartment.objects.filter().prefetch_related(
            Prefetch('id_dept_cl', queryset=TClientDepartment.objects.filter().select_related('id_client')))
        result_page = paginator.paginate_queryset(legal_entity, request)
        data = DepartmentSerializer(result_page, many=True).data
        return paginator.get_paginated_response(data)

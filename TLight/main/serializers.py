from rest_framework import serializers
from .models import *

class StatusSerializer(serializers.ModelSerializer):
    status_name = serializers.SerializerMethodField()

    def get_status_name(self, obj):
        return "Активный" if obj.status_name == True else "Не активный"

    class Meta:
        model = DStatus
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = TPhone
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = DGender
        fields = '__all__'


class MailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TMail
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    id_status = StatusSerializer(read_only=True)
    mail = MailSerializer(read_only=True)
    gender = GenderSerializer(read_only=True)

    class Meta:
        model = TClient
        fields = '__all__'


class ClientDepartmentSerializer(serializers.ModelSerializer):
    id_client = ClientSerializer(read_only=True, many=True)

    class Meta:
        model = TClientDepartment
        fields = ['id_client']


class DepartmentSerializer(serializers.ModelSerializer):
    id_dept_cl = ClientDepartmentSerializer(read_only=True)

    class Meta:
        model = TDepartment
        fields = '__all__'


class LegalEntityDepartmentSerializer(serializers.ModelSerializer):
    id_department = DepartmentSerializer(read_only=True, many=True)

    class Meta:
        model = TLegalEntityDepartment
        fields = ['id_department']


class LegalEntitySerializer(serializers.ModelSerializer):
    legal_dept = LegalEntityDepartmentSerializer(read_only=True)

    class Meta:
        model = TLegalEntity
        fields = '__all__'


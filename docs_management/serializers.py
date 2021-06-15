from rest_framework import serializers
from django.core import exceptions
from docs_management.models import UploadedDoc, ExtractedDoc


class UploadedDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedDoc
        fields = ("id", "uploaded_on", "storage_path", "status")


class UpdateStatusSerializer(serializers.ModelSerializer):
    status = serializers.IntegerField()

    class Meta:
        model = UploadedDoc
        fields = ["status"]

    def update_status(self, instance):
        instance.status = self.data["status"]

        return instance


class UpdateExtracedDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedDoc
        # fields = ["invoice_number", "summary"]
        exclude = ["uploaded_doc"]


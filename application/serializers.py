from rest_framework import serializers


class LegalTreeSerializer(serializers.Serializer):
    data = serializers.JSONField()

from rest_framework import serializers

from ieqtests.core.models import IQ, EQ, Test
from ieqtests.core.api.mixins import LoginCodeLookupMixin
from ieqtests.core.api.validators import LetterValidator


class TestSerializer(serializers.ModelSerializer):
    login_code = serializers.CharField(read_only=True)

    class Meta:
        model = Test
        fields = ('login_code',)


class IQSerializer(LoginCodeLookupMixin, serializers.ModelSerializer):
    results = serializers.IntegerField(min_value=0, max_value=50)

    class Meta:
        model = IQ
        fields = ('completed_at', 'results')
        extra_fields = {
            'completed_at': {
                'read_only': True
            }
        }


class EQSerializer(LoginCodeLookupMixin, serializers.ModelSerializer):
    results = serializers.ListField(
        child=serializers.CharField(min_length=1, max_length=1, validators=[LetterValidator()]),
        min_length=5,
        max_length=5
    )

    class Meta:
        model = EQ
        fields = ('completed_at', 'results')
        extra_fields = {
            'completed_at': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        results = validated_data.get('results')
        validated_data['results'] = ','.join(results)
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        results = instance.results.split(',')
        representation['results'] = results
        return representation


class ResultsSerializer(serializers.ModelSerializer):
    core_iq = IQSerializer(read_only=True, include_login_code=False)
    core_eq = EQSerializer(read_only=True, include_login_code=False)

    class Meta:
        model = Test
        fields = ('login_code', 'core_iq', 'core_eq')

from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ieqtests.core.models import Test
from ieqtests.core.models import IQ


class LoginCodeLookupMixin:

    def __init__(self, *args, **kwargs):
        include_login_code = kwargs.pop('include_login_code', True)
        super().__init__(*args, **kwargs)
        if include_login_code:
            self.fields['login_code'] = serializers.CharField(source='test.login_code')

    def create(self, validated_data):
        login_code = validated_data.pop('test')['login_code']
        qs = Test.objects.select_related('core_iq', 'core_eq')
        test = get_object_or_404(qs, login_code=login_code)
        if self.Meta.model is IQ:
            if hasattr(test, 'core_iq'):
                raise ValidationError("`login_code` must be unique.")
        else:
            if hasattr(test, 'core_eq'):
                raise ValidationError("`login_code` must be unique.")
        validated_data['test'] = test
        return super().create(validated_data)

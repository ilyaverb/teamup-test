from rest_framework import generics

from ieqtests.core.api.serializers import IQSerializer, EQSerializer, TestSerializer, ResultsSerializer
from ieqtests.core.models import IQ, EQ, Test


class TestCreateAPIView(generics.CreateAPIView):
    serializer_class = TestSerializer


class IQCreateAPIView(generics.CreateAPIView):
    serializer_class = IQSerializer


class EQCreateAPIView(generics.CreateAPIView):
    serializer_class = EQSerializer


class ResultsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ResultsSerializer
    queryset = Test.objects.select_related('core_iq', 'core_eq').all()
    lookup_field = 'login_code'
    lookup_url_kwarg = 'login_code'

from django.urls import path

from ieqtests.core.api.views import IQCreateAPIView, EQCreateAPIView, TestCreateAPIView, ResultsRetrieveAPIView

urlpatterns = [
    path(route='tests/', view=TestCreateAPIView.as_view(), name='create-test'),
    path(route='iq/', view=IQCreateAPIView.as_view(), name='save-iq-results'),
    path(route='eq/', view=EQCreateAPIView.as_view(), name='save-eq-results'),
    path(route='results/<str:login_code>/', view=ResultsRetrieveAPIView.as_view(), name='get-results')
]

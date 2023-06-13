from django.contrib import admin

from ieqtests.core.models import IQ, EQ, Test

admin.site.register([IQ, EQ, Test])

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('ieqtests.core.urls', 'core'), namespace='tests')),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

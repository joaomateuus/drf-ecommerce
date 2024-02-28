from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/v1/', include('core.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

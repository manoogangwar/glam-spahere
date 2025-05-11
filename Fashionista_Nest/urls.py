from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('fn_app.urls'))
    # Add your URL patterns here
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
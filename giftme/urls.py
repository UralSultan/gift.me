from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('timeline.urls')),
    path('', include('register.urls')),
    path('holidays/', include('holidays.urls')),
    path('about_user/', include('about_user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

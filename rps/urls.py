
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('profile/', include('user.urls')),
    path('recipe/', include('recipe.urls',namespace='recipe')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

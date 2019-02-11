from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.blog.admin import tenant_admin_site
from apps.blog.api import ArticleViewSet

router = routers.DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('nepex/tenant-admin/', tenant_admin_site.urls),

]

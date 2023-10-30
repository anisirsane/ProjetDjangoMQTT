from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from myapp.views import DataViewSet, publish_message

router = DefaultRouter()
router.register(r'data', DataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publish', publish_message, name='publish'),
    path('api/sensor-data/', DataViewSet.as_view({'get': 'list'}), name='data-list')
]

urlpatterns += router.urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import CategoryViewSet, ProductViewSet, ProductImageViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('product_images', ProductImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),

]

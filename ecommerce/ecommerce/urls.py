
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Welcome to the API!"})


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', root_view),  # 👈 Root URL
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]




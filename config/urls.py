"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Real Estate Sales & Leasing API",
        default_version="v1",
        description="API documentation for the Real Estate Sales & Leasing Management System",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls")),
    path("api/agents/", include("agents.urls")),
    path("api/listings/", include("listings.urls")),
    path("api/property-images/", include("property_images.urls")),
    path("api/favorites/", include("favorites.urls")),
    path("api/reviews/", include("reviews.urls"),),
    path("api/inspections/", include("inspections.urls")),
    
    
    path("swagger/",schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
    path("redoc/",schema_view.with_ui("redoc", cache_timeout=0),name="schema-redoc"),
    path("",schema_view.with_ui("redoc", cache_timeout=0),name="schema-redoc")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
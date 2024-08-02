from django.contrib import admin

from blog.views import BlogAPIView, BlogAPIView2, ListUsers

from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/listusers/', ListUsers.as_view()),
    path('api/v1/bloglist/', BlogAPIView.as_view()),
    path('api/v1/bloglist/<int:pk>/', BlogAPIView2.as_view()),
    # YOUR PATTERNS
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='My Project')
urlpatterns = [

    path('swagger-ui', schema_view),
    path('admin/', admin.site.urls),
    path('', include('user_management.urls')),
    path('', include('course_management.urls')),
    path('', include('notification_service.urls'))

]

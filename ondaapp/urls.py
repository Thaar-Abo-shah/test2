from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('data',views.data,name='data'),
    path('api',views.api,name='api'),
    path('csrf_token',views.csrf_token_view,name='csrf_token'),
    path('send',views.sendMail,name='send'),

] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
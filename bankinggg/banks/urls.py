from django.urls import path

from banks import views
from bankinggg import settings
from django.conf.urls.static import static
app_name='banks'

urlpatterns = [

    path('', views.hello, name='hello'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

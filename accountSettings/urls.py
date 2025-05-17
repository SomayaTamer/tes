from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('settings', views.runSettings, name='runsettings'),
    path ('about', views.about, name='about'),
    path ('', views.index, name='index')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

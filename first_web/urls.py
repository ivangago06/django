from django.contrib import admin
from django.urls import path

from first_web_app import views as core_views
from portafolio import views as portafolio_views

from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about-me/', core_views.about, name="about"),
    path('portafolio/', portafolio_views.portafolio, name="portafolio"),
    path('contacto/', core_views.contacto, name="contacto"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
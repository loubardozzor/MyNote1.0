"""
URL configuration for MyNotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from appunti import views, studenti_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('successo_caricamento/', views.pagina_di_successo_caricamento, name='pagina_di_successo_caricamento'),
    path('insuccesso_caricamento/', views.pagina_di_insuccesso_caricamento, name='pagina_di_insuccesso_caricamento'),
    path('materie/', views.materie_list, name='materie-list'),
    path('materie/<int:materia_id>/', views.materia_detail, name='materia-detail'),
    path('materie/<int:materia_id>/upload-appunto', views.upload_appunto, name='upload-appunto'),
    path('materie/<int:materia_id>/<int:appunto_id>/update-appunto', views.update_appunto, name= 'update-appunto'),
    path('materia/<int:materia_id>/<int:appunto_id>/update-appunto/update-appunto-name', views.update_appunto_name, name = 'update-appunto-name'),
    path('materia/<int:materia_id>/<int:appunto_id>/update-appunto/update-appunto-pdf',views.update_appunto_pdf, name = 'update-appunto-pdf'),
    path('materia/<int:materia_id>/<int:appunto_id>/update-appunto/update-appuntoNamePdf', views.update_appunto_namePdf, name = 'update-appunto-namePdf'),
    path('materia/<int:materia_id>/<int:appunto_id>', views.delete_appunto, name='delete-appunto'),
    path('materia/<int:materia_id>/<int:appunto_id>/', views.appunto_detail, name='appunto-detail'),
    path('materia/<int:materia_id>/<int:appunto_id>/download/', views.appunto_detail_download, name='appunto-detail-download' ),
    path('materia/<int:materia_id>/<int:appunto_id>/recenzionare', views.appunto_detail_recenzionare, name='appunto-detail-recenzionare'),
    path('materia/<int:materia_id>/<int:appunto_id>/votare', views.appunto_detail_votare, name='appunto-detail-votare'),

    path('studenti/', studenti_views.studenti_list, name = 'studenti-list'),
    path('studenti/<int:studenti_id>/', studenti_views.studente_detail, name='studente-detail'),
    path('', include('autenticazione.urls'))




]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

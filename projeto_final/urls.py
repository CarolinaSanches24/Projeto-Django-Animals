"""
URL configuration for projeto_final project.

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

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from cadastro_animal.views import criar_animal, AnimalViewSet, home, pesquisa_animal
from detalhesanimal.views import detalhes_animal
from django.views.generic.base import RedirectView
import uuid
from cadastro_animal import views

from django.contrib import admin
from gestao_adocao.views import adocao
from usuarios.views import editar_animal

router = routers.DefaultRouter()
router.register('cadastro', AnimalViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('', home),
    path('pesquisa/', pesquisa_animal, name='pesquisa_animal'),
    path('cadastrarAnimal/', criar_animal, name='criar_animal'),
    path('detalhes/<uuid:animal_id>/', detalhes_animal, name='detalhes_animal'),
    path('quem-somos/', views.quemsomos, name='quem_somos'),
    path('sejaparceiro/', views.sejaparceiro, name='sejaparceiro'),
    path('', include(router.urls)),
    path('adocao/', adocao),
    path('editar_animal/<uuid:animal_id>/',editar_animal,name='editar_animal')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
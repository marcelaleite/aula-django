"""feiras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home_view
from submissoes.views import ( submissoes_update_view, submissao_create_view, submissoes_list_view,
submissoes_detail_view,autor_create_view, autor_update_view, autor_list_view, autor_detail_view,submissao_delete_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('autor/', autor_list_view,name='autor-list'),
    path('autor/<int:pid>/', autor_detail_view,name='autor-detail'),
    path('autor/new/', autor_create_view,name='autor-create'),
    path('autor/<int:pid>/update/', autor_update_view,name='autor-update'),
    path('submissoes/', submissoes_list_view,name='submissoes-list'),
    path('submissoes/<int:pid>/', submissoes_detail_view,name='submissoes-detail'),
    path('submissoes/new/',submissao_create_view,name='submissoes-create'),
    path('submissoes/<int:pid>/update/', submissoes_update_view,name='submissoes-update'),
    path('submissoes/<int:pid>/delete/', submissao_delete_view,name='submissoes-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

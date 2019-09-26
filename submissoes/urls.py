from django.urls import path
from home.views import home_view
from submissoes.views import ( submissoes_update_view, submissao_create_view, submissoes_list_view,
submissoes_detail_view,autor_create_view, autor_update_view, autor_list_view, autor_detail_view,submissao_delete_view)

app_name = 'submissoes'

urlpatterns = [
    path('autor/', autor_list_view,name='autor-list'),
    path('autor/<int:pid>/', autor_detail_view,name='autor-detail'),
    path('autor/new/', autor_create_view,name='autor-create'),
    path('autor/<int:pid>/update/', autor_update_view,name='autor-update'),
    path('submissoes/', submissoes_list_view,name='submissoes-list'),
    path('submissoes/<int:pid>/', submissoes_detail_view,name='submissoes-detail'),
    path('submissoes/new/',submissao_create_view,name='submissoes-create'),
    path('submissoes/<int:pid>/update/', submissoes_update_view,name='submissoes-update'),
    path('submissoes/<int:pid>/delete/', submissao_delete_view,name='submissoes-delete'),
]

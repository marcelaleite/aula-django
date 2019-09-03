from django.contrib import admin

from .models import Autor
from .models import Submissao

admin.site.register(Autor)
admin.site.register(Submissao)

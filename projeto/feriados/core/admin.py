from django.contrib import admin
from core.models import FeriadoModel
from datetime import date

class FeriadoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia', 'mes', 'modificado_em', 'registrado_esse_ano')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome','dia','mes')
    list_filter = ('modificado_em',)

    def registrado_esse_ano(self, obj):
        hoje = date.today()
        return obj.modificado_em.year == hoje.year

    registrado_esse_ano.short_description = 'Registrado este ano'
    registrado_esse_ano.boolean = True

admin.site.register(FeriadoModel, FeriadoModelAdmin)

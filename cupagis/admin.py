from django.contrib import admin
from .models import Module, Cour, TP,Expose

class CourAdmin(admin.ModelAdmin):
    search_fields = ['titre_Cour']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "module":
            kwargs["queryset"] = Module.objects.filter(prof=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class TPAdmin(admin.ModelAdmin):
    search_fields = ['titre_TP']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "module":
            kwargs["queryset"] = Module.objects.filter(prof=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ExposeAdmin(admin.ModelAdmin):
    search_fields = ['sujet']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "module":
            kwargs["queryset"] = Module.objects.filter(prof=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Module)
admin.site.register(Cour, CourAdmin)
admin.site.register(TP, TPAdmin)
admin.site.register(Expose, ExposeAdmin)

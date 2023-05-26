from django.contrib import admin

from .models import Category, Genre, GenreTitle, Title


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "year",
        "description",
        "category"
    )
    list_editable = ("category",)
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(GenreTitle)

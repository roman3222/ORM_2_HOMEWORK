from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, TagsNews, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        scope_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                scope_count += 1
            if scope_count > 1:
                raise ValidationError('Основной тег может быть только один')
            if scope_count == 0:
                raise ValidationError('Укажите основной тег')
        return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]


@admin.register(TagsNews)
class TagNewsAdmin(admin.ModelAdmin):
    pass





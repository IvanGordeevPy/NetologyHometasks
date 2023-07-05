from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError
from .models import Article, ArticleScope, Scope

class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Тематики не определены')

        counter = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                counter += 1
            if counter > 1:
                raise ValidationError('Основная тема может быть только одна!')
        return super().clean()  

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleScope)
class ArticleScopeAdmin(admin.ModelAdmin):
    pass

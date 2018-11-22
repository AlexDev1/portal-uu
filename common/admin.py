from django.contrib import admin

from reversion.admin import VersionAdmin

from common.forms import BaseAdminForm


class BaseAdminContentModel(VersionAdmin):

    form = BaseAdminForm

    def get_queryset(self, request):
        return super(BaseAdminContentModel, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def get_form(self, request, obj=None, change=False, **kwargs):
        try:
            form = super(BaseAdminContentModel, self).get_form(request, obj, **kwargs)
            form.base_fields['name'].widget.attrs['size'] = '100'
            form.base_fields['name'].widget.attrs['class'] = ''
            form.base_fields['seo_title'].widget.attrs['size'] = '100'
            form.base_fields['seo_title'].widget.attrs['class'] = ''
            form.base_fields['description'].widget.attrs['rows'] = '2'
            form.base_fields['description'].widget.attrs['cols'] = '15'
            # form.base_fields['meta_keywords'].widget.attrs['rows'] = '2'
            # form.base_fields['meta_keywords'].widget.attrs['cols'] = '20'
        except:
            pass
        return form

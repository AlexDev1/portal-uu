import datetime
from django.contrib import admin
from django.urls import reverse
from filebrowser.base import FileObject

from app.admin_portal.import_uu import AdminMixinImport
from app.news.models import CommercialNewsType, News


# class TagsForm(forms.Form):
#     tags = TagField(widget=TagAutocomplete())


class NewsAdmin(AdminMixinImport, admin.ModelAdmin):

    list_display = ('preview_image', 'dt_mod', 'name', 'visible', 'on_main_page', 'update_date','adm_changeusr')
    #list_editable = ('visible', 'on_main_page')
    fields = ('dt_mod', 'name', 'seo_title', 'description',
              'content', 'image', 'visible',
              'on_main_page', 'commercial',
              'commercial_type', 'univer', 'suz',
              'seo_meta')
    search_fields = ['name', 'content']
    list_display_links = ['name']
    readonly_fields = ['update_date', 'adm_changeusr']
    date_hierarchy = 'dt_mod'
    list_filter = ('dt_mod',)
    raw_id_fields = ('univer',)
    # form = TagsForm

    class Meta:
        model = News

    def import_uu(self, request, *args, **kwargs):
        # На каждую модель нужно описать свои методы сохранения данных
        for _row in self.get_data_api():
            # print(_row['id'])
            try:
                News.objects.get(id=_row['id'])
            except News.DoesNotExist:
                row = self.model(**_row)
                if row.image:
                    row.image = FileObject(row.image)
                row.save()
                print("Add new News id: %s" % str(row.id))
            except Exception as ex:
                print(ex)
        return reverse('admin:%s' % self.urls[1].name)

    def save_model(self, request, obj, form, change):
        obj.adm_changeusr = request.user
        obj.update_date = datetime.datetime.now()
        obj.save()



admin.site.register(News, NewsAdmin)
admin.site.register(CommercialNewsType)
# admin.site.register(ItemComment)

# class SubscribersAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email')
#     search_fields = ('email', )
#     list_display_links = ['name']
#
#     class Meta:
#         model = Subscribers
# admin.site.register(Subscribers, SubscribersAdmin)

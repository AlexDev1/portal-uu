import datetime

from django.contrib import admin
from django.urls import reverse

from filebrowser.base import FileObject

from app.news.models import CommercialNewsType, News
from common.admin import BaseAdminContentModel


@admin.register(News)
class NewsAdmin(BaseAdminContentModel):

    list_display = ('preview_image', 'dt_mod', 'name', 'visible', 'on_main_page', 'modified',)
    #list_editable = ('visible', 'on_main_page')
    fields = ('dt_mod', 'name', 'description',
              'content', 'image', 'tags', ('visible', 'on_main_page', 'commercial'),
              'seo_title', 'seo_meta')
    search_fields = ['name', 'content']
    list_display_links = ['name', 'preview_image']
    readonly_fields = ['modified']
    date_hierarchy = 'dt_mod'
    list_filter = ('dt_mod',)

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


# admin.site.register(News, NewsAdmin)
# admin.site.register(CommercialNewsType)
# admin.site.register(ItemComment)

# class SubscribersAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email')
#     search_fields = ('email', )
#     list_display_links = ['name']
#
#     class Meta:
#         model = Subscribers
# admin.site.register(Subscribers, SubscribersAdmin)

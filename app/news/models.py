from django.db import models
from django.utils.safestring import mark_safe
from filebrowser.fields import FileBrowseField
from tagging.registry import register

from common.models import BaseContentModel
from users.models import User


class WidgetTags(models.Model):
    name = models.CharField(max_length=50)


register(WidgetTags)


class CommercialNewsType(models.Model):
    """если это комерческая новость, указывается тип
    (вуз, суз и т.п. с возможностью редактировать этот справлчник)
    """
    name = models.CharField('Название', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тип коммерческих новостей'
        verbose_name_plural = 'типы коммерческих новостей'


class News(BaseContentModel):
    """Новости"""

    image = FileBrowseField("Фото", format='image', directory='news',
                            max_length=255,
                            blank=True, null=True, db_index=True)
    on_main_page = models.BooleanField('На главную', default=False, db_index=True)

    commercial = models.BooleanField('Комерческая новость', default=False, db_index=True)

    show_count = models.IntegerField(
        verbose_name='Количество показов',
        default=0, db_index=True)

    def preview_image(self):
        try:
            thumbnail = self.image.version_generate('news_preview').url
        except TypeError:
            thumbnail = None  # if original img not exist
        except:
            thumbnail = None  # if original img not exist
        return mark_safe('<a href="%s/"><img src="%s"/></a>' % (self.id, thumbnail))

    preview_image.short_description = 'Фото'
    preview_image.allow_tags = True

    def get_absolute_url(self):
        # print self
        return ('news_view', None, {
            'year': self.dt_mod.year,
            'month': self.dt_mod.strftime('%m'),
            'day': self.dt_mod.day,
            'pk': self.pk
        })

    class Meta:
        ordering = ('-dt_mod',)
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

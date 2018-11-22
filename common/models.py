from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField
from meta.models import ModelMeta
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from taggit.managers import TaggableManager
from tinymce import models as tinymce_models

from common.utils.utils import unique_slug


class BaseVisibleManager(models.Manager):
    """
    Базовый менаджер моделей только опубликованных записей на сайте
    """
    def get_queryset(self):
        """Только обубликованные записи модели"""
        kwargs = {"visible": True}
        return super().get_queryset().filter(**kwargs)


class VisibleModel(models.Model):
    """ Абстрактная модель для публикации на сайте"""
    visible = models.BooleanField('Показывать на сайте?', default=False, db_index=True,
                                  help_text='Статус чернеовика')

    class Meta:
        abstract = True


class IndexedTimeStampedModel(models.Model):
    """Абстрактная модель Штампы времени"""
    created = AutoCreatedField(_('created'), db_index=True)
    modified = AutoLastModifiedField(_('modified'), db_index=True)

    class Meta:
        abstract = True


class SeoFieldsModel(models.Model):
    """Абстрактная модель СЕО-поля для мета-тегов"""
    seo_title = models.CharField('Заголовок(SEO)', null=True,
                                 blank=True, max_length=255,
                                 help_text='* !! НЕ обязательное поле, можно оставить пустым!')
    seo_meta = models.TextField('Meta(SEO)', null=True, blank=True,
                                help_text='Мета-описание страницы для сниппета')
    seo_keywords = models.TextField('Ключи', null=True, blank=True,
                                help_text='* !! НЕ обязательное поле, можно оставить пустым!')

    class Meta:
        abstract = True


class BaseContentModel(ModelMeta, VisibleModel, IndexedTimeStampedModel, SeoFieldsModel):
    """
    Базовая абстрактная модель для моделей с контентом
    """
    name = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Краткое описание')
    content = tinymce_models.HTMLField('Content')
    slug = models.SlugField('URL', null=True, blank=True, help_text='Можно оставлять пустып, авто из названия будет',
                            max_length=75)
    image = FileBrowseField(u"Картинка", format='image', directory='tribune',
                            max_length=255,
                            blank=True, null=True, db_index=True)
    # tags = TagAutocompleteField(blank=False, verbose_name='Теги')#ToDo Запилить ТЕГИ Select2!!!

    publish = BaseVisibleManager()
    objects = models.Manager()

    tags = TaggableManager()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    _metadata = {
        'use_og': 'true',
        'use_twitter': 'true',
        'use_title_tag': 'true',
        'use_facebook': 'true',
        'title': 'seo_title',
        'author': 'Учисьучись.РФ',
        'description': 'preview',
        'image': 'get_meta_image',
    }
    def get_meta_image(self):
        if self.image:
            return self.image.url

    def clean_slug(self):
        if not self.slug:
            self.slug = unique_slug(self.name[0:55], self)
        return self.slug

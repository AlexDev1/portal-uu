from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'app.admin_portal.pages'
    verbose_name = "Админ: Страницы на сайте"


class TaggitConfig(AppConfig):
    name = 'taggit'
    verbose_name = "Админ: Теги"


class FilebrowserConfig(AppConfig):
    name = 'filebrowser'
    verbose_name = "Файловый браузер"

# https://docs.djangoproject.com/en/1.10/ref/settings/

import os

from decouple import config  # noqa


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)


SITE_ID = 1

SECURE_HSTS_PRELOAD = True

DEBUG = True

ADMINS = (
    ('Admin', 'alexbog80@gmail.com'),
)

AUTH_USER_MODEL = 'users.User'

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'common.apps.FilebrowserConfig',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Packages
    'rest_framework',
    'django_extensions',
    'django_js_reverse',
    'webpack_loader',
    'import_export',
    'reversion',
    'easy_select2',
    'meta',
    'cookielaw',
    'common.apps.TaggitConfig',
    'tinymce',

    # Apps
    'common',
    'users',
    'app.news',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uuportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [base_dir_join('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'uuportal.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    base_dir_join('assets'),
)

# Webpack
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': False,  # on DEBUG should be False
        'STATS_FILE': base_dir_join('webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    },
    'JQUERY': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': 'jquery-webpack-stats.json',
    }
}

# FileBrowser
from uuportal.settings._filebrowser import *

# TinyMCE settings
# TINYMCE_COMPRESSOR = False
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,asciimath",
    'theme': "advanced",
    'language': "ru",
    # 'content_css': "/static/tinymce/tinymce.css",
    'visualblocks_default_state': "true",
    # Schema is HTML5 instead of default HTML4
    'schema': "html5",
    # 'valid_elements' : "",
    'style_formats_merge': "true",
    'extended_valid_elements' : "mark",
    'style_formats': [
        # {'title': u'Под катом', 'block': 'div','classes': 'b-cut'},
        # {'title': u'Файл .doc', 'inline' : 'span', 'classes' : 'b-file-extension_type_doc'},
        # {'title': u'Файл .xls', 'inline' : 'span', 'classes' : 'b-file-extension_type_xls'},
        # {'title': u'Файл .pdf', 'inline' : 'span', 'classes' : 'b-file-extension_type_pdf'},
        # {'title': u'Файл .ppt', 'inline' : 'span', 'classes' : 'b-file-extension_type_ppt'},
        # {'title': u'Файл .rar', 'inline' : 'span', 'classes' : 'b-file-extension_type_rar'},
        # {'title': u'Файл .zip', 'inline' : 'span', 'classes' : 'b-file-extension_type_zip'},
        {'title': u'Резиновая картинка', 'inline' : 'span', 'classes' : 'img-responsive'},
        {'title': u'Ключевик', 'inline' : 'mark', 'exact': 'false' },
        {'title': u'Круглая кнопка', 'selector': 'a', 'classes' : 'btn btn-sm btn-default btn-rounded'},
        {'title': u'Текст margin-b-15', 'selector': 'p', 'classes' : 'm-b-15'},
        {'title': u'Текст info', 'selector': 'p', 'classes' : 'text-info'},
        {'title': u'Текст warning', 'selector': 'p', 'classes' : 'text-warning'},
        {'title': u'Текст danger', 'selector': 'p', 'classes' : 'text-danger'},
        {'title': u'Текст text-right', 'selector': 'p,h1,h2,h3,h4', 'classes' : 'text-right'},
        {'title': u'Текст text-center', 'selector': 'p,h1,h2,h3,h4', 'classes' : 'text-center'},
        {'title': u'Текст text-justify', 'selector': 'p,h1,h2,h3,h4', 'classes' : 'text-justify'},
        # {'title': u'button-3d', 'selector': 'a', 'classes' : 'button button-default button-3d full-rounded'},

    ],
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,|,styleselect,formatselect",
    'theme_advanced_buttons2': "cut,copy,paste,pasteword,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,code,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,iespell,media,advhr,asciimathcharmap,|,fullscreen",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': "false",
    'function' : 'function(e) {e.onGetContent.add(function(e, o) {o.content = o.content.replace(/<span\ class="mark"[^>]*>([^>]+)<\/span>/ig,"<mark>$1</mark>");});',
    'AScgiloc': "http://www.imathas.com/editordemo/php/svgimg.php",
    'ASdloc': "%sstatic/tiny_mce/plugins/asciisvg/js/d.svg" % BASE_DIR,
    #'convert_newlines_to_brs' : "true",
    #'paste_auto_cleanup_on_paste' : "true",
    #'paste_remove_spans' : "true",
    # 'paste_remove_styles' : "true",
    #'paste_strip_class_attributes' : "none",
    #'paste_retain_style_properties' : "none",
}


# Celery
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

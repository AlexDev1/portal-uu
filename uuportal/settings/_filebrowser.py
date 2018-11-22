#FileBrowser Settings
FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)
# FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_VERSIONS_BASEDIR = '_versions_'
FILEBROWSER_VERSIONS = {
    'news_list_v2': {'verbose_name': 'News List', 'width': 255, 'height': 170, 'opts': 'crop'},
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'upscale'},
    'news_list': {'verbose_name': 'News List', 'width': 260, 'height': 230, 'opts': 'upscale crop'},
    'news_list_mainpage': {'verbose_name': 'News List', 'width': 170, 'height': 105, 'opts': 'upscale crop'},
    'news_list_mainpage2': {'verbose_name': 'News List', 'width': 200, 'height': 125, 'opts': 'upscale crop'},
    'blog_list_mainpage2': {'verbose_name': 'News List', 'width': 280, 'height': 490, 'opts': 'upscale crop'},
    'news_item': {'verbose_name': 'News Item', 'width': 430, 'height': '', 'opts': 'upscale'},
    'deals_list': {'verbose_name': 'Deals List', 'width': 80, 'height': 70, 'opts': 'upscale'},
    'news_preview': {'verbose_name': 'News List', 'width': 200, 'height': 100, 'opts': 'crop'},
    'banner_image': {'verbose_name': 'Banner Image', 'width': '', 'height': 300, 'opts': 'upscale crop'},
    'expert_logo': {'verbose_name': 'Expert Logo', 'width': 21, 'height': 21, 'opts': 'upscale crop'},
    'expert_image': {'verbose_name': 'Expert Image', 'width': 175, 'height': '', 'opts': 'upscale crop'},
    'expert_image_index': {'verbose_name': 'Expert Image Index', 'width': '', 'height': 150, 'opts': 'upscale crop'},
    'expert_list': {'verbose_name': 'Expert List', 'width': 80, 'height': 70, 'opts': 'upscale'},
    'catalog_category': {'verbose_name': 'Catalog Category', 'width': '', 'height': 57, 'opts': 'upscale crop'},
    'univer_logo': {'verbose_name': 'Catalog Item Tile', 'width': '', 'height': 120, 'opts': 'upscale'},
    'univer_item': {'verbose_name': 'Univer Item', 'width': 250, 'height': 250, 'opts': 'upscale crop'},
    'univer_olimp_logo': {'verbose_name': 'Univer Olimp', 'width': 105, 'height': 105, 'opts': 'upscale crop'},
    'univer_head': {'verbose_name': 'Univer Head', 'width': 150, 'height': 200, 'opts': 'upscale crop'},
    'blog_carusel': {'verbose_name': 'Blog Carusel', 'width': 315, 'height': 175, 'opts': 'upscale crop'},
    'library_list': {'verbose_name': 'Library List', 'width': 150, 'height': 100, 'opts': 'upscale crop'},
    'library_detail': {'verbose_name': 'Library Detail', 'width': 231, 'height': 350, 'opts': 'upscale crop'},
    'library_detail4': {'verbose_name': 'Library Detail2', 'width': 200, 'height': 300, 'opts': 'upscale crop'},
    'library_journal': {'verbose_name': 'Library Journal', 'width': 231, 'height': 350, 'opts': 'upscale crop'},
    'library_journal2': {'verbose_name': 'Library Journal2', 'width': 300, 'height': 450, 'opts': 'upscale crop'},
    'contest_index': {'verbose_name': 'Contest Index', 'width': 165, 'height': 165, 'opts': 'upscale crop'},
    'contest_list2': {'verbose_name': 'Contest List', 'width': 262, 'height': 215, 'opts': 'upscale crop'},
    'contest_list300x250': {'verbose_name': 'Contest List', 'width': 300, 'height': 250, 'opts': 'upscale crop'},
    'contest_detail': {'verbose_name': 'Contest List', 'width': 845, 'height': 550, 'opts': 'upscale crop'},
    'contest_cover': {'verbose_name': 'Contest Cover', 'width': 240, 'height': 300, 'opts': 'upscale crop'},
    'contest_header': {'verbose_name': 'Contest List', 'width': 845, 'height': 68, 'opts': 'upscale crop'},
    'blog_item_list': {'verbose_name': 'Catalog Item List', 'width': 60, 'height': 40, 'opts': ['crop', 'upscale']},
    'catalog_item_list': {'verbose_name': 'Catalog Item List', 'width': '', 'height': 70, 'opts': 'upscale crop'},
    'univer_logo_detail': {'verbose_name': 'Catalog Item Detail', 'width': '', 'height': 180, 'opts': 'upscale'},
    'catalog_item_detail_thumb': {'verbose_name': 'Catalog Item Detail Thumb', 'width': 65, 'height': 65, 'opts': 'upscale crop'},
    'test-icon': {'verbose_name': 'Test Online Icon', 'width': 64, 'height': 64, 'opts': 'upscale crop'},
    'speciality-group-icon': {'verbose_name': 'Speciality group icon', 'width': 128, 'height': 128, 'opts': 'upscale crop'},
    'speciality-group-icon2': {'verbose_name': 'Speciality group icon', 'width': 268, 'height': 268, 'opts': 'upscale crop'},

    'author_image_admin' : {'verbose_name': 'Author Image Admin', 'width': 60, 'height': 80, 'opts': 'upscale crop'},
    'author_image': {'verbose_name': 'Author Image', 'width': 120, 'height': 160, 'opts': 'upscale crop'},
    'author_image_small2': {'verbose_name': 'Author Image', 'width': 50, 'height': 70, 'opts': 'upscale crop'},
    'author_image_blog': {'verbose_name': 'Author Image', 'width': 60, 'height': 80, 'opts': 'upscale crop'},

    #'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
    'subject_icon': {'verbose_name': 'subject icon', 'width': 50, 'height': '50', 'opts': 'crop'},
    'party_site_header_news': {'verbose_name': 'party_site_header_news', 'width': '', 'height': 300, 'opts': 'upscale'},
    'bannerbackground_image': {'verbose_name': 'bannerbackground_image', 'width': '237', 'height': 142, 'opts': 'upscale'},
}

FILEBROWSER_ADMIN_THUMBNAIL = 'fb_thumb'

FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.swf', '.flv'],
    'Document': ['.pdf', '.doc', '.pps', '.rtf', '.txt', '.xls', '.csv', '.odt', '.ods', '.ppt', '.pptx', '.docx', '.xlsx','.opf', '.chm', '.wpd', '.sxw', '.docm', '.sxc', '.wks'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p'],
    'Code': ['.html', '.py', '.js', '.css', '.xml'],
    'Archive': ['.7z', '.rar', '.zip', '.tar', '.gz']
}
FILEBROWSER_SELECT_FORMATS = {
    'file': ['Folder', 'Image', 'Document', 'Video', 'Audio', 'Archive','Code'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
    'archive': ['Archive'],
    'code': ['Code'],
}

# THUMBNAIL_ENGINE = 'sorl_watermarker.engines.pil_engine.Engine'
# THUMBNAIL_WATERMARK = 'uu_watermark.png'
# THUMBNAIL_WATERMARK_OPACITY = 1
FILE_UPLOAD_PERMISSIONS = 0o755
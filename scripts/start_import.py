import os
import urllib.request
from urllib.error import URLError

from django.apps import apps
from django.core import management
from django.core.management.commands import loaddata

from filebrowser.base import FileObject
from requests import HTTPError
from rest_framework.parsers import JSONParser


# from app.library.models import Library
# from app.news.models import News
# from app.regions.models import Region


class ImportApi(object):
    model = None
    model_name = ''
    change_list_template = 'admin/importuu/change_list.html'
    api_urls = 'http://127.0.0.1:8001/api/'

    def load_fixture(self):
        print("Start load_fixture for app!")
        for file in os.listdir('dump'):
            if file.endswith(".json"):
                result = management.call_command(loaddata.Command(), 'dump/{0}'.format(file), verbosity=0)
                print('Load json: {0} - SUCCESS!'.format(file.title()))

    def get_data_api(self):
        try:
            url_get = '%s%s/?format=json' % (self.api_urls, self.model_name.lower())
            print('Send request: {0}'.format(url_get))
            api_data = urllib.request.urlopen(url_get)
            data = JSONParser().parse(api_data)
        except HTTPError as ex:
            print('ERROR HTTP {0}'.format(ex))
            data = []
        except URLError as ex:
            print('ERROR HTTP {0}'.format(ex))
            data = []
        return data

    def get_model_apps(self, app_name=None, model_name=None):
        model = apps.get_model(app_name, model_name)
        return model

    def import_default(self, app_name=None, model_name=None):
        """Regions"""
        self.model = apps.get_model(app_name, model_name)
        self.model_name = model_name
        data = self.get_data_api()
        print("{1} objects: {0}".format(len(data), self.model_name))
        if data:
            for _row in data:
                # print(_row)
                try:
                    self.model.objects.get(id=_row['id'])
                except self.model.DoesNotExist:
                    try:
                        row = self.model(**_row)
                        row.save()
                    except Exception as ex:
                        print("Error save {0} \n ERROR: {1}".format(self.model_name, ex))
                except Exception as ex:
                    print(ex)
        else:
            print("No DATA get_data for app {0}!".format(self.model_name))
        print("End get_data for app {0} in SUCCESS!".format(self.model_name))

    def import_pages(self, app_name=None, model_name=None):
        """Regions"""
        self.model = apps.get_model(app_name, model_name)
        self.model_name = model_name
        data = self.get_data_api()
        print("{1} objects: {0}".format(len(data), self.model_name))
        if data:
            for _row in data:
                # print(_row)
                try:
                    self.model.objects.get(id=_row['id'])
                except self.model.DoesNotExist:
                    try:
                        row = self.model(**_row)
                        row.save(force_insert = True)
                    except Exception as ex:
                        print("Error save {0} \n ERROR: {1}".format(self.model_name, ex))
                except Exception as ex:
                    print(ex)
        else:
            print("No DATA get_data for app {0}!".format(self.model_name))
        print("End get_data for app {0} in SUCCESS!".format(self.model_name))

    def import_News(self, app_name=None, model_name=None):
        from app.news.models import News
        """News"""
        self.model = apps.get_model(app_name, model_name)
        self.model_name = model_name
        data = self.get_data_api()
        if data:
            print("{1} objects: {0}".format(len(data), self.model_name))
            for _row in data:
                # print(_row['id'])
                try:
                    News.objects.get(id=_row['id'])
                except News.DoesNotExist:
                    try:
                        row = News()
                        row.name = _row['name']

                        row.seo_title = _row['seo_title']
                        row.seo_meta = _row['seo_meta']
                        row.description = _row['description']
                        row.content = _row['content']
                        row.on_main_page = _row['on_main_page']
                        row.tags = _row['tags']
                        row.visible = True
                        if _row['image']:
                            row.image = FileObject(_row['image'])
                        row.save()
                    except Exception as ex:
                        print("Error save News \n ERROR: %s" % ex)
                except Exception as ex:
                    print(ex)
        else:
            print("No DATA get_data for app {0}!".format(self.model_name))
        print("End get_data for app {0} in SUCCESS!".format(self.model_name))

    def import_user(self, app_name=None, model_name=None):
        """Users"""
        self.model = apps.get_model(app_name, model_name)
        self.model_name = model_name
        data = self.get_data_api()
        print("{1} objects: {0}".format(len(data), self.model_name))
        if data:
            for _row in data:
                # print(_row)
                try:
                    self.model.objects.get(id=_row['id'])
                except self.model.DoesNotExist:
                    try:
                        row = self.model(**_row)
                        if row.avatar:
                            row.avatar = FileObject(row.avatar)
                        row.save()
                    except Exception as ex:
                        print("Error save {0} \n ERROR: {1}".format(self.model_name, ex))
                except Exception as ex:
                    print(ex)
        print("End get_data for app {0} in SUCCESS!".format(self.model_name))

    def import_library(self, app_name=None, model_name=None):
        """Library"""
        self.model = apps.get_model(app_name, model_name)
        self.model_name = model_name
        data = self.get_data_api()

        if data:
            print("{1} objects: {0}".format(len(data), self.model_name))
            for _row in data:
                # print(_row)
                try:
                    self.model.objects.get(id=_row['id'])
                except self.model.DoesNotExist:
                    try:
                        subjects = _row['subjects']
                        levels = _row['levels']
                        authors = _row['authors']
                        print(subjects)
                        row = Library(
                            id = _row['id'],
                            material_type_id=_row['material_type_id'],
                            publisher_id=_row['publisher_id'],
                            format_id=_row['format_id'],
                            language_id=_row['language_id'],
                            adm_changeusr_id=_row['adm_changeusr_id'],
                            title=_row['title'],
                            description=_row['description'],
                            count_pages = _row['count_pages'],
                            cover=_row['cover'],
                            ISBN=_row['ISBN'],
                            datetime = _row['datetime'],
                            status=_row['status'],
                            file = _row['file'],
                            visible = _row['visible'],
                            comment = _row['comment'],
                            show_count = _row['show_count'],
                            agv_rating = _row['agv_rating'],
                            update_date = _row['update_date'],
                            adm_changedt = _row['adm_changedt'],
                        )

                        print(row.file)

                        row.subjects.add(subjects)
                        # row.levels.set(levels)
                        # row.authors.set(authors)
                        #row.save()
                    except Exception as ex:
                        print("Error save {0} \n ERROR: {1}".format(self.model_name, ex))
                except Exception as ex:
                    print(ex)
        else:
            print("No DATA get_data for app {0}!".format(self.model_name))
        print("End get_data for app {0} in SUCCESS!".format(self.model_name))

    def import_Blog(self, app_name=None, model_name=None):
        """Blog"""
        self.model = apps.get_model(app_name, model_name)
        self.model_name = model_name
        # data = self.get_data_api()
        try:
            url_get = '%s%s/?format=json' % (self.api_urls, self.model_name.lower())
            print('Send request: {0}'.format(url_get))
            api_data = urllib.request.urlopen(url_get)
            data = JSONParser().parse(api_data)
        except HTTPError as ex:
            print('ERROR HTTP {0}'.format(ex))
            data = []
        except URLError as ex:
            print('ERROR HTTP {0}'.format(ex))
            data = []

        self.model_name = 'Post'
        if data:
            print("{1} objects: {0}".format(len(data), self.model_name))
            for _row in data:
                # print(_row['id'])
                try:
                    self.model.objects.get(id=_row['id'])
                except self.model.DoesNotExist:
                    try:
                        row = self.model(**_row)
                        if row.image:
                            row.image = FileObject(row.image)
                        row.save()
                    except Exception as ex:
                        print("Error save News \n ERROR: %s" % ex)
                except Exception as ex:
                    print(ex)
        else:
            print("No DATA get_data for app {0}!".format(self.model_name))
        print("End get_data for app {0} in SUCCESS!".format(self.model_name))


def run():
    get_data = ImportApi()
    get_data.load_fixture()

    print("Start get_data for api {0}!".format(get_data.api_urls))
    get_data.import_News(app_name='news', model_name='News')
    #get_data.import_Blog(app_name='tribune', model_name='Item')
    # get_data.import_pages(app_name='pages', model_name='Page')
    # News
    #get_data.import_News(app_name='news', model_name='News')
    # get_data.import_user(app_name='users', model_name='User')
    # get_data.import_default(app_name='regions', model_name='Region')
    # import_city(get_data, app_name='regions', model_name='City')
    # get_data.import_default(app_name='testing', model_name='TestObjects') ToDo Не загрузились картинки
    #get_data.import_library(app_name='library', model_name='Library')


def import_univer(self, app_name=None, model_name=None):
    """Unver"""
    self.model = apps.get_model(app_name, model_name)
    self.model_name = model_name
    data = self.get_data_api()
    print("{1} objects: {0}".format(len(data), self.model_name))
    if data:
        for _row in data:
            # print(_row['id'])
            try:
                self.model.objects.get(id=_row['id'])
            except self.model.DoesNotExist:
                try:
                    row = self.model.objects.create(
                        id=_row['id'],
                        name=_row['name'],
                        visible=_row['visible'],
                        region=Region.objects.get(id=_row['region'])
                    )

                    row.save()
                except Exception as ex:
                    print("Error save {0} \n ERROR: {1}".format(self.model_name, ex))
            except Exception as ex:
                print(ex)
    print("End get_data for app {0} in SUCCESS!".format(self.model_name))


def import_city(self, app_name=None, model_name=None):
    """Regions"""
    self.model = apps.get_model(app_name, model_name)
    self.model_name = model_name
    data = self.get_data_api()
    print("{1} objects: {0}".format(len(data), self.model_name))
    if data:
        for _row in data:
            # print(_row['id'])
            try:
                self.model.objects.get(id=_row['id'])
            except self.model.DoesNotExist:
                try:
                    row = self.model.objects.create(
                        id=_row['id'],
                        name=_row['name'],
                        visible=_row['visible'],
                        region=Region.objects.get(id=_row['region'])
                    )

                    row.save()
                except Exception as ex:
                    print("Error save {0} \n ERROR: {1}".format(self.model_name, ex))
            except Exception as ex:
                print(ex)
    print("End get_data for app {0} in SUCCESS!".format(self.model_name))

# # -*- coding: utf-8 -*-
# import csv
# import locale
# import logging
# import os
# import re
# import StringIO
# import sys
# import time
# from datetime import datetime, timedelta
# from types import *
#
# import celery
# import psycopg2
# from celery.task import periodic_task
# from celery.task.schedules import crontab
# #from dbmail import send_db_mail
# #from dbmail.models import MailTemplate
# from django.conf import settings
# from django.contrib.sites.models import Site
# from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
# from django.core.mail import send_mail
# from django.urls import reverse
# from django.utils import timezone
# from grab import Grab, UploadContent, UploadFile
# from PIL import Image
#
# import settings
#
# from ..news.models import News, Subscribers


# from bs4 import BeautifulSoup
# from celery.schedules import crontab
# from django.template.loader import get_template
# from ..cabinet.models import FAQparser
# from django.template import Context
# from ..cabinet.views import send_mail_of_list
# import urlparse
# import urllib2
# import datetime

#(crontab(hour="15", minute="30", day_of_week="*"))timedelta(seconds=300)
# @celery.decorators.periodic_task(run_every=(crontab(hour="10", minute="30", day_of_week="fri")))
# def News_Send_Subscribs():
#     from django.utils import dateformat
#     try:
#         MailTemplate.objects.get(slug='news_subsc')
#     except ObjectDoesNotExist:
#         MailTemplate.objects.create(
#             name="Рассылка новстей",
#             subject="Новости культуры и образования",
#             message="{% extends 'emails/base_html.html' %} {% block content %} {% include 'emails/news_subs.html' %} {% endblock %}",
#             is_html=True,
#             slug='news_subsc',
#             is_admin=False,
#             is_active=True,
#             interval=500
#         )
#     month_names = [
#         u'января',
#         u'февраля',
#         u'марта',
#         u'апреля',
#         u'мая',
#         u'июня',
#         u'июля',
#         u'августа',
#         u'сентября',
#         u'октября',
#         u'ноября',
#         u'декабря',
#     ]
#
#     #locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#     formatted_date = u'%s %s %sг.' % (str(timezone.now().day),month_names[timezone.now().month-1], timezone.now().year )
#     Subscrib = []
#     team = u'Новости культуры и образования от %s' % (formatted_date)
#     queryset = News.objects.filter(dt_mod__lte=timezone.now(), dt_mod__gte=datetime.now()-timedelta(days=5)).order_by('-dt_mod')
#
#     if queryset:
#         try:
#             for email in Subscribers.objects.filter(is_involved=True):
#                 Subscrib.append(email.email)
#                 send_db_mail(
#                     'news_subsc',
#                     email.email,
#                     {'choises': queryset, 'teame': team, 'user': email.name }
#                 )
#                 #messages.success(request, "Создана рассылка и поставлена в очередь. Кол-во писем: %s" % (len(Subscrib)))
#         except Exception as ex:
#             #pass
#             print ex.args
#             #messages.error(request, "Ошибка отправки писем: %s" % str(ex.message))



# '''
# pip install -U Grab
# '''
# '''Парсер Новостей с сайта Минобрнауки'''
# @celery.decorators.periodic_task(run_every=(crontab(hour="05", minute="00", day_of_week="*")))
# def news_parser_minobr():
#     siteUrl = "http://xn--80abucjiibhv9a.xn--p1ai/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/"
#     #urls = Geturl.GrabMinobr(siteUrl)
#     g = Grab()
#     g.setup(timeout=5, connect_timeout=3)
#     #g.load_proxylist('html/file.txt', 'text_file', auto_init=True, auto_change=True, proxy_type='http')
#     g.go(siteUrl)
#     #page = open('html/edunetwork.html')
#     if g:
#         result = []
#         urlsBlocs = g.doc.select('//div[@class="news-item"]//h3//a')
#         #urls = pq(page)
#         #urlsBlocs = urls('div.news-section div.news-item h3 a')
#         urlsElement = []
#         for i in range(len(urlsBlocs)):
#             urlsElement.append(urlsBlocs.selector_list[i].attr("data-url"))
#     if urlsElement:
#         res = []
#         for url in urlsElement:
#             siteHost = "http://xn--80abucjiibhv9a.xn--p1ai"
#             #urlpage ='http://xn--80abucjiibhv9a.xn--p1ai/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/ajax/5811'
#             urlpage = siteHost+url
#             page = Grab()
#             page.setup(timeout=5, connect_timeout=3)
#             page.go(urlpage)
#             #page = loadPage('file:///Users/aleks/gitwork/Parser/html/len.html')
#             #print 'Получили html'
#             if page:
#                 result = []
#                 #d = pq(page)
#                 #print page.doc.body
#                 #d = pq(etree.fromstring(page))
#                 #print "PAGE--END"
#                 #title = ''
#                 #bloccatalog = d('div.reader-wrap-in')
#                 tagtitle = page.doc.select('//div[@class="r-content"]//h2').text()
#                 #print g.tree
#                 #tagtitle = d('div.reader-wrap-in div.r-content h2').text
#                 if (tagtitle==None):
#                     send_db_mail('news_subsc', 'halyvinav@sp-corp.ru',
#                                  {'teame': "Ошибка парсинга с Минобрнауки", 'user': "Не найден тег Н2" })
#                     return False
#
#                 else:
#                     title = tagtitle
#
#                 try:
#                     #print title
#                     item = News.allobjects.get(name=title)
#                     #print item
#                 except ObjectDoesNotExist:
#                     '''Обрабатываем картинку'''
#                     try:
#                         tagimg = page.doc.select('//div[@class="enlarge-holder"]//img').attr('src')
#                         #print tagimg
#                         gi = Grab()
#                         gi.go(tagimg)   #топаем по ссылке в теге img
#                         img = Image.open(StringIO.StringIO(gi.response.body)) #Передаем объект
#                         imgSize = img.size #Получаем размер изображения
#                         imgPath = 'media/uploads/news/dorms/'+os.path.basename(tagimg)
#                         imgSave = 'uploads/news/dorms/'+os.path.basename(tagimg)
#                         #extList = get_match(e_pattern,text) #получаем тип (расширение) файла
#                         if imgSize > (64,64): #И если размер картинки подходящий
#                             with open(imgPath, 'wb') as f:
#                                 #print 'with'
#                                 f.write(gi.response.body)
#                                 f.close()     #то сохраняем картинку
#                     except Exception as ex:
#                         print ex.args
#                         imgSave = ''
#
#                     try:
#                         tagabout = page.doc.select('//div[@class="r-article"]//p//span').text()
#                     except:
#                         try:
#                             tagabout = page.doc.select('//div[@class="r-article"]//p').text()
#                         except:
#                             tagabout = ''
#
#                     tagbody = ''
#                     try:
#                         body = page.doc.select('//div[@class="r-article"]').text()
#                         for elem in page.doc.select('//div[@class="r-article"]'):
#                             #print elem.text()
#                             tagbody =tagbody+'<p>'+elem.text()+'</p>'
#                     except:
#                         try:
#                             tagbody = ''
#                             # for elem in page.doc.select('//div[@class="r-article"]//p'):
#                             #     #print elem.text()
#                             #     tagbody =tagbody+'<p>'+elem.text()+'</p>'
#                         except:
#                             pass
#                     tagbody = tagbody+u'<br><p>Источник: <a href="http://xn--80abucjiibhv9a.xn--p1ai/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8" rel="nofollow"> минобрнауки.рф</a></p>'
#                     try:
#                         #print imgSave
#                         news_item = News()
#                         news_item.name = title
#                         news_item.description = tagabout
#                         news_item.content = tagbody
#                         news_item.image = imgSave
#                         news_item.visible = False
#                         news_item.save()
#                         self_admin_url = reverse('admin:news_news_change', args=(news_item.pk,))
#                         site = str(Site.objects.get_current())[:-1]
#                         adsolute_admin_url = site + self_admin_url
#                         message = u"%s \n %s \n Проверить: %s " % (
#                             news_item.name, news_item.description, adsolute_admin_url)
#                         # send_mail(
#                         #     u'**SYSTEM-SEND-MAIL** - Добавлена новость с сайта Минобрнауки', message,
#                         #     settings.DEFAULT_FROM_EMAIL,
#                         #     ['halyvinav@sp-corp.ru', ], fail_silently=False)
#                         # send_mail(
#                         #     u'**SYSTEM-SEND-MAIL** - Добавлена новость с сайта Минобрнауки', message,
#                         #     settings.DEFAULT_FROM_EMAIL,
#                         #     ['alexbog80@gmail.com', ], fail_silently=False)
#                     except Exception as ex:
#                         #print ex.args
#                         #send_db_mail('news_subsc','alexbog80@gmail.com',
#                         #             {'teame': "Ошибка парсинга с Минобрнауки", 'user': "Ошибка сохранения данных: "+str(ex.args) }
#                         #print ex.args
#                         send_db_mail('news_subsc','halyvinav@sp-corp.ru',
#                                      {'teame': "Ошибка парсинга с Минобрнауки", 'user': "Ошибка сохранения данных: "+str(ex.args) })
#
#
# '''Парсер Новостей с сайта http://www.fadm.gov.ru/news/'''
# @celery.decorators.periodic_task(run_every=(crontab(hour="05", minute="10", day_of_week="*")))
# def news_parser_fadmgovrur():
#     siteUrl = "http://www.fadm.gov.ru/news/"
#     #urls = Geturl.GrabMinobr(siteUrl)
#     g = Grab()
#     g.setup(timeout=5, connect_timeout=3)
#     #g.load_proxylist('html/file.txt', 'text_file', auto_init=True, auto_change=True, proxy_type='http')
#     g.go(siteUrl)
#     #page = open('html/edunetwork.html')
#     if g:
#         result = []
#         urlsBlocs = g.doc.select('//div[@class="article-body"]//h2//a')
#         #urls = pq(page)
#         #urlsBlocs = urls('div.news-section div.news-item h3 a')
#         urlsElement = []
#         for i in range(len(urlsBlocs)):
#             urlsElement.append(urlsBlocs.selector_list[i].attr("href"))
#     if urlsElement:
#         res = []
#         nn = 0
#         for url in urlsElement:
#             regnews = False
#             siteHost = "http://www.fadm.gov.ru"
#             #urlpage ='http://xn--80abucjiibhv9a.xn--p1ai/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/ajax/5811'
#             urlpage = siteHost+url
#             page = Grab()
#             page.setup(timeout=5, connect_timeout=3)
#             page.go(urlpage)
#             #page = loadPage('file:///Users/aleks/gitwork/Parser/html/len.html')
#             #print 'Получили html'
#             nn = nn + 1
#             if nn == 10:
#                 break
#             if page:
#                 result = []
#                 #d = pq(page)
#                 #print page.doc.body
#                 #d = pq(etree.fromstring(page))
#                 #print "PAGE--END"
#                 #title = ''
#                 #bloccatalog = d('div.reader-wrap-in')
#                 try:
#                     tagtitle = page.doc.select('//div[@class="inner_content"]//h3').text()
#                 except:
#                     regnews = True
#                     tagtitle = page.doc.select('//ul[@class="breadcrumb-navigation"]//li[3]').text()
#                 #print g.tree
#                 #tagtitle = d('div.reader-wrap-in div.r-content h2').text
#                 if (tagtitle==None):
#                     send_db_mail('news_subsc', 'halyvinav@sp-corp.ru',
#                                  {'teame': "Ошибка парсинга с Минобрнауки", 'user': "Не найден тег Н3" })
#                     return False
#
#                 else:
#                     title = tagtitle
#
#                 try:
#                     #print title
#                     item = News.allobjects.get(name=title)
#                     #print item
#                 except ObjectDoesNotExist:
#                     '''Обрабатываем картинку'''
#                     try:
#                         tagimg = siteHost+page.doc.select('//img[@class="detail_picture"]').attr('src')
#                         #print tagimg
#                         gi = Grab()
#                         gi.go(tagimg)   #топаем по ссылке в теге img
#                         img = Image.open(StringIO.StringIO(gi.response.body)) #Передаем объект
#                         imgSize = img.size #Получаем размер изображения
#                         imgPath = 'media/uploads/news/dorms/'+os.path.basename(tagimg)
#                         imgSave = 'uploads/news/dorms/'+os.path.basename(tagimg)
#                         #extList = get_match(e_pattern,text) #получаем тип (расширение) файла
#                         if imgSize > (32,32): #И если размер картинки подходящий
#                             with open(imgPath, 'wb') as f:
#                                 #print 'with'
#                                 f.write(gi.response.body)
#                                 f.close()     #то сохраняем картинку
#                     except Exception as ex:
#                         print "ERROR SAVE IMAGE"
#                         imgSave = ''
#
#                     try:
#                         tagabout = page.doc.select('//div[@class="inner_content"]//div//b').text()
#                     except:
#                         tagabout = ''
#
#                     tagbody = ''
#                     try:
#                         if regnews:
#                             for elem in page.doc.select('//div[@class="news-detail"]//div'):
#                                 it = elem.node()
#                                 print it
#                                 if it.attrib.values()<>['news-date-time']:
#                                     if len(elem.text())>0:
#                                         tagbody =tagbody+'<p>'+elem.text()+'</p>'
#                         else:
#                             #body = page.doc.select('//div[@class="inner_content"]').text()
#                             for elem in page.doc.select('//div[@class="inner_content"]//div'):
#                                 it = elem.node()
#                                 if it.attrib.values()<>['date']:
#                                     if len(elem.text())>0:
#                                         if tagabout == '':
#                                             tagabout = elem.text()
#                                         tagbody =tagbody+'<p>'+elem.text()+'</p>'
#                     except:
#                         try:
#                             tagbody = ''
#                             # for elem in page.doc.select('//div[@class="r-article"]//p'):
#                             #     #print elem.text()
#                             #     tagbody =tagbody+'<p>'+elem.text()+'</p>'
#                         except:
#                             pass
#                     tagbody = tagbody+u'<br><p>Источник: <a href="http://www.fadm.gov.ru/news/32208/" rel="nofollow"> Росмолодежь</a></p>'
#                     try:
#                         #print imgSave
#                         news_item = News()
#                         news_item.name = title
#                         news_item.description = tagabout
#                         news_item.content = tagbody
#                         news_item.image = imgSave
#                         news_item.visible = False
#                         news_item.save()
#                         self_admin_url = reverse('admin:news_news_change', args=(news_item.pk,))
#                         site = str(Site.objects.get_current())[:-1]
#                         adsolute_admin_url = site + self_admin_url
#                         message = u"%s \n %s \n Проверить: %s " % (
#                             news_item.name, news_item.description, adsolute_admin_url)
#                         # send_mail(
#                         #     u'**SYSTEM-SEND-MAIL** - Добавлена новость с сайта http://www.fadm.gov.ru/news/', message,
#                         #     settings.DEFAULT_FROM_EMAIL,
#                         #     ['halyvinav@sp-corp.ru', ], fail_silently=False)
#
#                         # send_mail(
#                         #     u'**SYSTEM-SEND-MAIL** - Добавлена новость с сайта Минобрнауки', message,
#                         #     settings.DEFAULT_FROM_EMAIL,
#                         #     ['alexbog80@gmail.com', ], fail_silently=False)
#                     except Exception as ex:
#                         #print ex.args
#                         send_db_mail('news_subsc','halyvinav@sp-corp.ru',
#                                      {'teame': "Ошибка парсинга с Минобрнауки", 'user': "Ошибка сохранения данных: "+str(ex.args) })

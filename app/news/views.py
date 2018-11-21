import datetime
import json
from datetime import datetime, timedelta


from django import forms
from django.contrib.syndication.views import Feed
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import HttpResponse, redirect, render, get_object_or_404
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from tagging.views import TaggedObjectList

from app.admin_portal.models import PromoPage
from website.views import ContextMixinMenu
from app.news.models import News
from ..tribune.models import Item as tribuneItems
from ..tribune.views import GetBlogCarusel


class NewsList(ListView, ContextMixinMenu):
    # Список новостей
    model = News
    template_name = 'news/news_list_new.html'
    paginate_by = 10

    # pages_forward = 2
    # page_slice = None

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     self.page_slice = get_paginator_slice(request, self.paginate_by,
    #                                           self.pages_forward)
    #     return super(NewsList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        '''
        список новостей может быть выведен с привязкой к месяцу и году
        либо просто так
        '''
        data = {}
        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)
        if year and month:
            qs = News.objects.filter(dt_mod__year=year,
                                     dt_mod__month=month).order_by('-dt_mod')
        else:
            qs = News.objects.filter(dt_mod__lte=timezone.now(), ).order_by('-dt_mod')[:self.paginate_by]
        data['news'] = qs
        return data

    def get(self, request, *args, **kwargs):
        data = self.get_queryset(request=request)
        # types = data['types']
        news = data['news']
        more_button: bool = True

        years = News.objects.filter(dt_mod__lte=timezone.now()).datetimes('dt_mod', 'year', order='DESC')
        months = News.objects.filter(dt_mod__lte=timezone.now()).datetimes('dt_mod', 'month')

        if request.GET.get("q"):
            query = request.GET.get("q")
            news = News.objects.filter(dt_mod__lte=timezone.now()).order_by('-dt_mod')
            news = news.filter(name__icontains=query)
            more_button = False
        year = int(self.kwargs.get('year', 0))
        month = int(self.kwargs.get('month', 0))
        # newsabout = tribuneItems.objects.all()[:10]
        last_blog = tribuneItems.objects.filter(date_create__lte=timezone.now(), visible=True)[:5]
        dt_today = timezone.now()
        if year and month:
            news = news.filter(dt_mod__year=year,
                               dt_mod__month=month, dt_mod__lte=timezone.now()).order_by('-dt_mod')
            more_button = False
        if year > 0:
            return render(request, self.template_name,
                          {'last_blog': last_blog,
                           "news": news, 'year': year, 'month': datetime(year, month, 1),
                           'years': years, 'months': months, 'dt_today': dt_today,
                           'more_button': more_button})
        else:
            return render(request, self.template_name,
                          {'last_blog': last_blog,
                           "news": news, 'years': years, 'months': months, 'page_obj': self.paginator_class,
                           'more_button': more_button})

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context = GetBlogCarusel(context)
        context['page_slice'] = self.page_slice
        year = int(self.kwargs.get('year', 0))
        month = int(self.kwargs.get('month', 0))
        if year > 0 and month > 0:
            context['date_filter'] = datetime.date(year, month, 1)
            if year != datetime.date.today().year:
                context['show_year'] = True
            # context['current_month'] = datetime.date(year, month, 1)
            context['time_news'] = True
        else:
            context['more_button'] = True

        return context


def news_items_more(request, offset=0):
    if offset == 0:
        news = News.objects.filter(dt_mod__lte=timezone.now(),
                                   dt_mod__gte=datetime.now() - timedelta(days=10)).order_by('-dt_mod')

    else:
        news = News.objects.filter(dt_mod__lte=timezone.now()).order_by('-dt_mod')[offset:][:10]

    return render(request, 'news/news_list_more.html', {
        'news': news
    })


class NewsView(DetailView, ContextMixinMenu):
    # показ новости
    model = News
    context_object_name = 'news'
    template_name = 'news/news_post.html'

    def get_object(self, queryset=None):
        object = super(NewsView, self).get_object()
        object.show_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        '''
        новость выводится с привязкой к месяцу и году
        '''
        context = super(NewsView, self).get_context_data(**kwargs)
        context['years'] = News.objects.filter().datetimes(
            'dt_mod', 'year', order='DESC')
        context['months'] = News.objects.filter().datetimes('dt_mod', 'month')

        context = GetBlogCarusel(context)
        context['newsabout'] = News.objects.filter(dt_mod__lte=timezone.now()).exclude(pk=self.kwargs['pk']).order_by(
            '-dt_mod')[:8]
        return context


class LatestNewsFeed(Feed):
    title = 'Учисьучись.рф'
    link = '/news/rss/'
    description = "Новости Учисьучись.рф"

    def items(self):
        return News.objects.filter(dt_mod__lte=timezone.now()).order_by('-dt_mod')[:8]

    def item_title(self, item):
        return item.name

    def item_pubdate(self, item):
        return item.dt_mod

    def item_link(self, item):
        return item.get_absolute_url()


class TaggetNews(TaggedObjectList, ContextMixinMenu):
    template_name = 'news/news_list_tag.html'
    model = News
    paginate_by = 25
    allow_empty = True


def news_pk(request, pk):
    try:
        redirect_object = get_object_or_404(News, pk=pk)
        return redirect(redirect_object)
    except:
        return HttpResponseNotFound()

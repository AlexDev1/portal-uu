from django.views.generic.base import ContextMixin, TemplateView


class ContextMixinMeta(ContextMixin):
    """Mixin Form Meta object view"""
    def get_context_data(self, **kwargs):
        context = super(ContextMixinMeta, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context


class ContextMixinMenu(ContextMixin):
    """Главный контекст для шаблонов"""
    def get_context_data(self, **kwargs):
        context = super(ContextMixinMenu, self).get_context_data(**kwargs)
        # context['last_blog'] = Post.objects.filter(is_adv=False)[0:3]
        # context['popular_blog'] = popular_week_post()
        # context['last_news'] = News.objects.all()[0:5]
        # dt_today = datetime.date.today()
        # context['promo'] = PromoPage.objects.filter(dt_start__lte=dt_today).filter(dt_end__gte=dt_today)
        # if context['promo']:
        #     context['FeedbackForm'] = FeedbackForm()
        # #Пользователи\Онлайн\Зарегистрированных
        # guests_cached = cache.get('guests_online', {})
        # users_cached = cache.get('users_online', {})
        # users_online = users_cached and User.objects.filter(id__in=users_cached.keys()) or []
        # context['online_count'] = len(users_online)
        # context['users_online'] = users_online
        # context['guest_count'] = len(guests_cached)

        return context


class IndexView(TemplateView, ContextMixinMenu):
    template_name = "index.html"


class SearchGoogle(TemplateView, ContextMixinMenu):
    """Поиск на сайте"""
    template_name = 'search_site.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchGoogle, self).get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('q')
        return context

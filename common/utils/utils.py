from django.utils.text import slugify


def unique_slug(value, instance):
    slug = slugify(value)

    queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    next = 2
    while queryset.filter(slug=slug):
        end = '-%s' % next
        slug = '%s%s' % (slug, end)
        next += 1

    return slug

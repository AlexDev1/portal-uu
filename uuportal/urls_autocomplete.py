from django.urls import path

from dal import autocomplete
from taggit.models import Tag


urlpatterns = [
    path(
        'tags/',
        autocomplete.Select2QuerySetView.as_view(
            queryset=Tag.objects.all(),
        ),
        name='select2_taggit',
    ),

]

from django.forms import ModelForm

from dal import autocomplete


class BaseAdminForm(ModelForm):
    class Meta:
        widgets = {
            'tags': autocomplete.TagSelect2('select2_taggit')
        }
    fields = '__all__'

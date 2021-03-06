from django.contrib.sites.models import get_current_site
from django.utils.functional import SimpleLazyObject


def frontend(request):
    return {
        'site': SimpleLazyObject(lambda: get_current_site(request)),
    }

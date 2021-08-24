from django.db import models
from .models import Song
import django_filters

class SongFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Song
        fields = [ 'name', 'artist', 'album' ]
    
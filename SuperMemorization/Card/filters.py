import django_filters
from .models import User


class UsersFitler(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username')

    class Meta:
        model = User
        fields = ['username']



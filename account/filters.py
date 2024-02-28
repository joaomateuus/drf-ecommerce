from django_filters import filterset, widgets
from account import filter_options as options
from account import models

class CharInFilter(filterset.BaseInFilter, filterset.CharFilter):
    pass


class NumberInFilter(filterset.BaseInFilter, filterset.NumberFilter):
    pass


class UserFilter(filterset.FilterSet):
    id = filterset.NumberFilter(lookup_expr=options.EXACT)
    email = filterset.CharFilter(lookup_expr=options.ICONTAINS)
    full_name = filterset.CharFilter(lookup_expr=options.ICONTAINS)
    is_active = filterset.BooleanFilter(widget=widgets.BooleanWidget)
    is_superuser = filterset.BooleanFilter(widget=widgets.BooleanWidget)
    is_staff = filterset.BooleanFilter(widget=widgets.BooleanWidget)
    
    class Meta:
        model = models.User
        fields = [
            'id',
            'email',
            'full_name',
            'is_active',
            'is_superuser',
            'is_staff'
        ]


class UserAdressFilter(filterset.FilterSet):
    id = filterset.NumberFilter(lookup_expr=options.EXACT)
    user = filterset.NumberFilter(lookup_expr=options.EXACT, field_name='user__id')
    user_by_name = filterset.CharFilter(lookup_expr=options.ICONTAINS, field_name='user__full_name')
    adress = filterset.CharFilter(lookup_expr=options.ICONTAINS)
    city = filterset.CharFilter(lookup_expr=options.ICONTAINS)
    country = filterset.CharFilter(lookup_expr=options.ICONTAINS)
    postal_code = filterset.CharFilter(lookup_expr=options.ICONTAINS)
    phone = filterset.CharFilter(lookup_expr=options.ICONTAINS)
    
    class Meta:
        model = models.UserAdress
        fields = [
            'id',
            'user',
            'user_by_name',
            'adress',
            'city',
            'country',
            'postal_code',
            'phone'
        ]
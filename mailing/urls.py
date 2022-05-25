# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import MirrorView, SubscriptionsManagementView

__all__ = [
    'app_name', 'urlpatterns',
]

app_name = 'mailing'
urlpatterns = [
    re_path(
        r'^mirror/(?P<signed_pk>[0-9]+:[a-zA-Z0-9_-]+)/$',
        MirrorView.as_view(),
        name='mirror',
    ),
    re_path(
        r'^subscriptions/(?P<signed_email>.+:[a-zA-Z0-9_-]+)/$',
        SubscriptionsManagementView.as_view(),
        name='subscriptions',
    ),
]

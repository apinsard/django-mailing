# -*- coding: utf-8 -*-
# Copyright (c) 2016 Aladom SAS & Hosting Dvpt SAS
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import (
    CampaignMailHeader, MailHeader, Subscription, SubscriptionType,
    CampaignStaticAttachment, MailStaticAttachment,
)

__all__ = [
    'CampaignMailHeaderForm', 'MailHeaderForm', 'SubscriptionsManagementForm',
    'CampaignStaticAttachmentForm', 'MailStaticAttachmentForm',
]


class CampaignMailHeaderForm(forms.ModelForm):

    class Meta:
        model = CampaignMailHeader
        fields = '__all__'
        widgets = {
            'value': forms.Textarea(attrs={'rows': 1}),
        }
        help_texts = {
            'value': _("May contain template variables."),
        }


class MailHeaderForm(forms.ModelForm):

    class Meta:
        model = MailHeader
        fields = '__all__'
        widgets = {
            'value': forms.Textarea(attrs={'rows': 1}),
        }


class SubscriptionsManagementForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.email = kwargs.pop('email')
        subscription_types = SubscriptionType.objects.all()
        for subscription_type in subscription_types:
            self.base_fields['subscribed_{}'.format(subscription_type.pk)] = (
                forms.BooleanField(
                    label=subscription_type.name,
                    help_text=subscription_type.description,
                    initial=subscription_type.is_subscribed(self.email),
                    required=False,
                )
            )
        super().__init__(*args, **kwargs)

    def save(self):
        subscriptions = {
            s.subscription_type_id: s
            for s in Subscription.objects.filter(email=self.email)
        }

        for field, value in self.cleaned_data.items():
            pk = int(field.split('_')[-1])
            if pk not in subscriptions:
                Subscription(email=self.email, subscription_type_id=pk,
                             subscribed=value).save()
            elif subscriptions[pk].subscribed != value:
                subscriptions[pk].subscribed = value
                subscriptions[pk].save()


class CampaignStaticAttachmentForm(forms.ModelForm):

    class Meta:
        model = CampaignStaticAttachment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachment'].widget.choices.insert(0, ('', '------'))


class MailStaticAttachmentForm(forms.ModelForm):

    class Meta:
        model = MailStaticAttachment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachment'].widget.choices.insert(0, ('', '------'))

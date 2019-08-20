# coding: utf-8
from __future__ import unicode_literals

from datetime import date
from dateutil.relativedelta import relativedelta

from django.conf import settings
from django.db import models
from django.utils.six import python_2_unicode_compatible


def get_lifetime_in_days():
    return getattr(
        settings,
        'EMAIL_LOGGER_LIFETIME_IN_DAYS',
        15
    )


@python_2_unicode_compatible
class EmailLog(models.Model):
    """The main idea is store the email event, not the content."""
    subject = models.TextField(blank=True)
    from_email = models.TextField(blank=True)
    recipient_list = models.TextField(blank=True)
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created in'
    )
    failed = models.NullBooleanField(default=None)

    def __str__(self):
        return 'Email sent from {} to {} ({})'.format(
            self.from_email,
            self.recipient_list,
            self.creation_date
        )


def clean_old_email_logs():
    u"""Clear the old mail logs.

    Look at settings.EMAIL_LOGGER_LIFETIME_IN_DAYS variable.
    """
    base_date = date.today() - relativedelta(days=int(get_lifetime_in_days()))
    logs = EmailLog.objects.filter(creation_date__lt=base_date)
    return logs.delete()

# coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import send_mail
from django.test import TestCase

from email_logger.models import EmailLog


class LoggerTestCase(TestCase):
    def setUp(self):
        settings.EMAIL_BACKEND = 'email_logger.backends.EmailLoggerBackend'
        settings.EMAIL_LOGGER_BASE = 'django.core.mail.backends.dummy.EmailBackend'

    def test_send_mail(self):
        initial_count = EmailLog.objects.count()
        send_mail(
            subject='logger',
            message='message',
            from_email='logger@anyhost.com',
            recipient_list=['anymail@anyhost.com'],
            fail_silently=False
        )
        self.assertEqual(initial_count + 1, EmailLog.objects.count())

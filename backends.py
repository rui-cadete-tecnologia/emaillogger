# coding: utf-8

import time

from django.apps import apps
from django.conf import settings


def get_class(kls):
    """
    Converts a string to a class.
    Courtesy: http://stackoverflow.com/questions/452969/does-python-have-an-equivalent-to-java-class-forname/452981#452981
    """
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


# 'EmailBackendClass' is the class the really sends the email
# the logger class will inherits from it
EmailBackendClass = get_class(settings.EMAIL_LOGGER_BASE)


class EmailLoggerBackend(EmailBackendClass):
    """Do the same of EmailBackend but logs the email."""

    def send_messages(self, email_messages):
        """Logging the email."""
        logger_model = apps.get_model('email_logger', 'EmailLog')
        sent_count = 0
        for message in email_messages:
            emaillog = logger_model.objects.create(
                subject=message.subject,
                from_email=message.from_email,
                recipient_list=u','.join(message.recipients()),
                failed=True
            )
            sent = super(EmailLoggerBackend, self).send_messages([message])
            if sent:
                sent_count += sent
                emaillog.failed = False
                emaillog.save()
        time.sleep(0.5)
        return sent_count

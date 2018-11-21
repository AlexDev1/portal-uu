# -*- coding: utf-8 -*-
import re

from django.core.validators import validate_email
from django.db import models


def emails(value):
    return filter(
        lambda x: bool(x.strip()), re.split(r'[,|;]?\s?', value or ''))


class MultiEmailField(models.CharField):
    def validate(self, value, model_instance):
        super(MultiEmailField, self).validate(value, model_instance)
        for email in emails(value):
            validate_email(email)

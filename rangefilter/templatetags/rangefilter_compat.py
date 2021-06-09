# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django

from django.template import Library

from django.templatetags.static import static as _static

register = Library()


@register.simple_tag()
def static(path):
    return _static(path)

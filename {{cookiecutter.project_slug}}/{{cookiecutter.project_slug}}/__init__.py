# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_short_description }}"""
# :copyright: (c) {{ cookiecutter.year }}, {{ cookiecutter.full_name }}.
#             All rights reserved.
# :license:   BSD (3 Clause), see LICENSE for more details.

from __future__ import absolute_import, unicode_literals

from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info = version_info_t(1, 0, 0, '', '')

__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = '{{ cookiecutter.full_name }}'
__contact__ = '{{ cookiecutter.email }}'
__homepage__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}'
__docformat__ = 'restructuredtext'

# -eof meta-

__all__ = []

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sanyam Khurana'
SITENAME = u'MozPacers'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/mozpacers/'),
    ('twitter', 'https://twitter.com/mozpacers'),
    ('facebook', 'https://facebook.com/mozpacers'),
    ('youtube', 'https://youtube.com/mozpacers'),
    ('slack', 'https://mozpacers.slack.com'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom settings for pure theme
THEME = 'theme/pure'
COVER_IMG_URL = 'images/firefox_os_logo.png'
TAGLINE = 'Mozilla Delhi Community'

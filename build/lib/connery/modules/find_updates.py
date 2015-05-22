# coding=utf8
"""
find_updates.py - Update checking module for Connery.

This is separated from version.py, so that it can be easily overridden by
distribution packagers, and they can check their repositories rather than the
Connery website.
"""
# Copyright 2014, Edward D. Powell, embolalia.net
# Licensed under the Eiffel Forum License 2.
from __future__ import unicode_literals

import json
import re

import connery
import connery.module
import connery.web

wait_time = 24 * 60 * 60  # check once per day
startup_check_run = False
version_url = 'http://connery.dftba.net/latest.json'
message = (
    'A new Connery version, {}, is available. I am running {}. Please update ' +
    'me. Full release notes at {}.'
)


def parse_version(version):
    return re.match('(\d+)\.(\d+)\.(\d+)(?:-\S+)?', version).groups()


@connery.module.event('001')
@connery.module.event('251')
@connery.module.rule('.*')
def startup_version_check(bot, trigger):
    global startup_check_run
    if not startup_check_run:
        startup_check_run = True
        check_version(bot)


@connery.module.interval(wait_time)
def check_version(bot):
    version = parse_version(connery.__version__)

    info = json.loads(connery.web.get(version_url))
    latest = info['version']
    notes = info['release_notes']
    latest_version = parse_version(latest)

    if version < latest_version:
        bot.msg(bot.config.core.owner,
                message.format(latest, connery.__version__, notes))

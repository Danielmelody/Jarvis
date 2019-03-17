#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this code is for appending a correct week date of last week, then I start to write my works.

import datetime
import os

if __name__ == '__main__':
    today = datetime.date.today()
    last_sunday = (today - datetime.timedelta(days=(today.weekday() + 1)))
    lastweek = '\r\n' + str(last_sunday - datetime.timedelta(days=7)) + \
        '~' + str(last_sunday - datetime.timedelta(days=2)) + '\r\n'
    f = open(os.path.expanduser('~/Documents/Weekly Report.md'), 'a')
    f.write(lastweek)
    f.close()

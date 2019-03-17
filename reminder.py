#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A short mac reminder when focusing on screen works

from Foundation import NSUserNotification
from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotificationDefaultSoundName
import argparse
import time


def main():
    parser = argparse.ArgumentParser(description=' -t TITLE -m MESSAGE')
    parser.add_argument('-t', '--title', action='store',
                        default='通知', type=lambda s: unicode(s, 'utf8'))
    parser.add_argument('-m', '--message', action='store',
                        default='...', type=lambda s: unicode(s, 'utf8'))
    parser.add_argument('-d', '--delay', action='store', default=0)
    parser.add_argument('--no-sound', action='store_false', default=True,
                        dest='sound')

    args = parser.parse_args()
    time.sleep(float(args.delay) * 60)
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(args.title + " " + args.delay + u"分钟以前")
    notification.setInformativeText_(args.message)
    if args.sound:
        notification.setSoundName_(NSUserNotificationDefaultSoundName)

    print "test"

    center = NSUserNotificationCenter.defaultUserNotificationCenter()
    center.deliverNotification_(notification)
    # notification.


if __name__ == '__main__':
    main()

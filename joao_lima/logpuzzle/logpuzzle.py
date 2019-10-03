#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os # noqa
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6" # noqa
"""


def _open_file(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text


def _create_html(images_names):
    f = open("index.html", "w+")
    for img_name in images_names:
        f.write('<img src="{}"/>\n'.format(img_name))
    f.close()
    return "index.html - OK"


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    host = "http://" + filename[filename.find("_") + 1:]
    logs = _open_file(filename)
    urls = re.findall(r'"GET(.+).+HTTP.+"', logs)
    urls = [host+url.strip() for url in urls if 'puzzle' in url]
    urls.sort()
    return urls


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    name_number = 0
    image_name_list = []
    if dest_dir[-1] != '/':
        dest_dir += '/'
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for url in img_urls:
        image_name = dest_dir+"image"+str(name_number)+".jpg"
        urllib.urlretrieve(url, image_name)
        name_number += 1
        image_name_list.append(image_name)
    _create_html(image_name_list)


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()

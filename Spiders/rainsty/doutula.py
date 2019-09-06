#!/usr/bin/python
# encoding: utf-8

"""
@author: rainsty
@file:   doutula.py
@time:   2019-09-05 22:48:52
@description:
"""

import requests
from lxml import etree
from datetime import datetime

FILE_PATH = '../../Test/file/picture/'


def get_url_results(url, xpath):
    resp = requests.get(url)
    html = etree.HTML(resp.text.encode(resp.encoding).decode('utf-8'))
    return html.xpath(xpath)


def get_html_xpath(url, xpath):
    results = get_url_results(url, xpath)
    result = list()
    for r in results:
        try:
            result.append(r.attrib)
        except BaseException as e:
            print(e)

    return result


def get_html_url_xpath(url, xpath):
    results = get_url_results(url, xpath)
    result = list()
    for r in results:
        try:
            download_img(r.attrib['src'])
        except BaseException as e:
            print(e)

    return result


def download_img(url):
    try:
        filename = url.split('/')[-1]
        file_path = FILE_PATH + filename

        with open(file_path, 'wb') as w:
            w.write(requests.get(url).content)

    except BaseException as e:
        print('download_img error: ' + str(e))


def main():
    urls = [r['href'] for r in get_html_xpath('https://www.doutula.com/', '//div[@class="col-sm-9 center-wrap"]/a')]

    for url in urls:
        res = get_html_url_xpath(url, '//li[@class="list-group-item"]//a/img')
        try:
            for r in res:
                download_img(r['src'])
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    start = datetime.now()
    main()
    end = datetime.now()
    print('Sum the time is: {}S'.format(end - start))


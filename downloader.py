# -*- coding: utf-8 -*-
"""
Скрипт для скачивания комиксов c acomics.ru.
"""

import requests
import re

comix_title = 'triangle'
comix_url = 'http://acomics.ru/~' + comix_title + '/'
first_page_number = 1
last_page_number = 327


def page_download(comix_link, page_num):
    page_url = comix_link + str(page_num)
    response = requests.get(page_url, cookies={'ageRestrict': '17'})
    page_content = response.content.decode('utf-8')
    link_regex = '/upload/!c/.+/' + comix_title + '/' + ('%6d' % page_num).replace(' ', '0') + '-.+.jpg'
    img_link = re.search(link_regex, page_content)
    img_link_abs = 'http://acomics.ru' + img_link.group()

    img_code = requests.get(img_link_abs)

    img_file = open(str(page_num) + '.jpg', 'w')
    img_file.write(img_code.content)
    img_file.close()

    print(img_link_abs)

page_number = first_page_number

while page_number <= last_page_number:
    page_download(comix_url, page_number)
    page_number += 1
from urllib.request import urlopen
from xml.etree.ElementTree import parse

#var_url = urlopen('https://smekm.ru/yml_get/ctfjm41hwzr')


def yandex_id(var_url):
    var_url = urlopen(var_url)
    xmldoc = parse(var_url)
    lst = []
    for item in xmldoc.iterfind('shop/offers/offer'):
        lst.append(item.attrib['id'])
    return lst


def google_id(var_url):
    var_url = urlopen(var_url)
    xmldoc = parse(var_url)
    lst = []
    for item in xmldoc.iterfind('channel/item'):
        lst.append(item[0].text)
    return lst

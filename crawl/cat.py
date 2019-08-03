from crawl.http.request import DownLoader


def cat_simple(site_name):
    return DownLoader.request(site_name)


def cat_selenium(site_name):
    return

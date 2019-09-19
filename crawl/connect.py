import requests
import time
from requests import ConnectionError as rConnectionError
import logging


class Connect:
    @classmethod
    def request(cls, url, max_repeat=1):
        res = None
        for i in range(max_repeat):
            try:
                res = requests.get(url)
                break
            except rConnectionError as e:
                if i == 3:
                    logging.info('fail! {0}'.format(url))
                    return None
                time.sleep(5)
        return res.text

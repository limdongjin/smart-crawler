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
                if i > 0:
                    logging.info('success')
                break
            except rConnectionError as e:
                if i == 3:
                    logging.info('fail!')
                    return None
                logging.info('re-try connect. n={0}'.format(i))
                logging.info(url)
                time.sleep(5)
        return res.text

# smart-crawller

## Introduction

- useful packages or code blocks for crawling
    - table crawling package
    - multiprocessing crawling with selenium, pool,..
- provide code snippets to crawl specific sites
    - Korea bill(law) information system(의안정보시스템): 법안 정보
- Another reason for doing this project is the purpose of studying.
- current version is alpha stage. so this project not stable. 
- if you want contribute, welcome Issue or PR 

## Install and Configuration

1. install selenium, chrome. 
 - [**selenium(chrome-driver)**](https://sites.google.com/a/chromium.org/chromedriver/home)
 - [**chrome**](https://www.google.com/intl/ko/chrome/)
 
2. install dependencies
```bash
$ python setup.py install
```

3. configure **config/selenium.py**. 
```python

# Configuration Selenium
config_selenium = {
    'headless': False, 
    # or True
    
    'chrome_driver_binary': 'your-selenium-chrome-driver-binary'
    # ex) /Users/imdongjin/Downloads/chromedriver
}
```

4. re-build to apply changes

```python
$ python setup.py install
```

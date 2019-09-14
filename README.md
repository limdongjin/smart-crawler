# smart-crawler

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

### **step1. install selenium, chrome.** 
 - [**selenium(chrome-driver)**](https://sites.google.com/a/chromium.org/chromedriver/home)
 - [**chrome**](https://www.google.com/intl/ko/chrome/)

<br>

mac, windows, linux(gui)
 - go to above link and download **chrome**, **chromedriver** file
 - be careful: chrome version, chromedriver version
    - If you are using Chrome version 77, please download ChromeDriver 77.0.3865.40
    - If you are using Chrome version 76, please download ChromeDriver 76.0.3809.126
    - If you are using Chrome version 75, please download ChromeDriver 75.0.3770.140  
 - if chromedriver download success, unzip chromedriver and store. 
 
 <br>
 
linux(cli)
 ```bash
# chrome install
$ ./sh/install_chrome_linux64.sh

# chromedriver install
$ ./sh/install_chromedriver_linux64.sh
```
### **step2. install dependencies**
```bash
$ python setup.py install
```

### **step3. configure `config/setting.py`.** 
```python

# Configuration Selenium
config_selenium = {
    'headless': False, 
    # or True
    # if your computer is Non-GUI OS 
    # must change 'headless' option True. 
    
    'chrome_driver_binary': 'your-selenium-chrome-driver-binary-path'
    # ex) /Users/imdongjin/Downloads/chromedriver
    # ex) /usr/local/bin/chromedriver
}
```

### **step4. re-build to apply changes**

```bash
$ python setup.py install
```

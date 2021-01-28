# Query Automation in Incremental Search

The Query Automation in Incremental Search (**QAIS**) is a data collection system that captures network traffic while an English or Chinese query is typed into an incremental search website.

QAIS consists of a keystroke replayer based on PyAutoGUI, browser automation with Selenium WebDriver, and a packet sniffer driven by Scapy.

## Installation

1. Download and install the right version of WebDriver for your browser.

* [ChromeDriver](https://chromedriver.chromium.org/downloads) for Google Chrome
* [GeckoDriver](https://github.com/mozilla/geckodriver/releases/) for Mozilla Firefox
* [WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) for Microsoft Edge

2. Use pip with Python 3.x to install the QAIS package:

```sh
pip install https://github.com/ld258166011/QAIS/archive/main.zip
```


## Usage

The QAIS python package provides a command `qais` to perform the automation and capture process. Use the command `qais` to get the help message:

```
usage: qais [-h] [--chinese] [--bigrams PATH] [--broswer NAME] [--click]
            [-f FILE]
            website query

Query Automation in Incremental Search

positional arguments:
  website         currently support Google, Tmall, Facebook, Baidu, Yahoo,
                  Wikipedia, Csdn, Twitch, Bing.
  query           search query to be entered. Currently support English and
                  Chinese.

optional arguments:
  -h, --help      show this help message and exit
  --chinese       Chinese query entered using Pinyin IME.
  --bigrams PATH  filename of the bigram timing model (csv format).
  --broswer NAME  currently support Chrome, Firefox, and Edge, default is
                  Chrome.
  --click         click the search box once before entering the query.
  -f FILE         filename of the captured traffic, default is pkts.pcap.
```

Use the following command to run QAIS with default optional arguments:

```sh
qais website query
```


## Examples

1. Search for the English query "the lazy dog" in Google:

```sh
qais Google "the lazy dog"
```

2. Search for the Chinese query "大黄蜂" in Baidu:

```sh
qais Baidu 大黄蜂 --chinese
```


## Related repository

* [ISTD](https://github.com/ld258166011/ISTD): the traffic dataset that contains 32.4k samples of English and Chinese queries captured on 9 incremental search websites.

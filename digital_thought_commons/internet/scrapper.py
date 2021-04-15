from selenium import webdriver as wd
from selenium.webdriver.chrome import webdriver
from urllib3.util import parse_url

import logging


class Scrapper():

    def __init__(self, tor_proxy=None, internet_proxy=None, headless=True, chromium_driver="chromedriver") -> None:
        super().__init__()

        if tor_proxy is None:
            tor_proxy = '--proxy-server=socks5://127.0.0.1:9150'
        self.tor_proxy = tor_proxy
        self.internet_proxy = internet_proxy
        self.headless = headless
        self.chromium_driver = chromium_driver

        self.tor_scrapper = self.__initialise_scrapper(proxy=self.tor_proxy)
        self.internet_scrapper = self.__initialise_scrapper(proxy=self.internet_proxy)

    def __initialise_scrapper(self, proxy) -> webdriver.WebDriver:
        options = wd.ChromeOptions()
        if self.headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.headless = True
        if proxy:
            options.add_argument(proxy)
        return wd.Chrome(executable_path=self.chromium_driver, options=options)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        self.tor_scrapper.close()
        self.internet_scrapper.close()

    def scrapper(self, url) -> webdriver.WebDriver:
        try:
            parsed_url = parse_url(url)
            if parsed_url.host.lower().endswith('.onion'):
                logging.debug(f'URL: {url} required the TOR Requester')
                return self.tor_scrapper
            else:
                logging.debug(f'URL: {url} required the Internet Requester')
                return self.internet_scrapper
        except Exception as ex:
            logging.exception(str(ex))
            logging.error(f'Unable to determine requester from URL: {url}')

    def get(self, url: str, force_tor=False) -> webdriver.WebDriver:
        if force_tor:
            chosen_scrapper = self.tor_scrapper
        else:
            chosen_scrapper = self.scrapper(url)
        chosen_scrapper.get(url=url)
        return chosen_scrapper

import unittest

from digital_thought_commons.internet import scrapper


class TestScrapper(unittest.TestCase):

    def test_forced_tor_scrapper(self):
        with scrapper.Scrapper(chromium_driver=r'./chromedriver', headless=True) as scrapper_instance:
            tor_response = scrapper_instance.get('https://whatismyipaddress.com/', force_tor=True)
            internet = scrapper_instance.get('https://whatismyipaddress.com/')
            self.assertNotEqual(tor_response.find_element_by_class_name("ip-address").text, internet.find_element_by_class_name("ip-address").text)

    def test_scrapper(self):
        with scrapper.Scrapper(chromium_driver=r'./chromedriver', headless=True) as scrapper_instance:
            tor_response = scrapper_instance.get('https://whatismyipaddress.com/', force_tor=False)
            internet = scrapper_instance.get('https://whatismyipaddress.com/')
            self.assertEqual(tor_response.find_element_by_class_name("ip-address").text, internet.find_element_by_class_name("ip-address").text)

    def test_forced_tor_scrapper_non_headless(self):
        with scrapper.Scrapper(chromium_driver=r'./chromedriver', headless=False) as scrapper_instance:
            tor_response = scrapper_instance.get('https://whatismyipaddress.com/', force_tor=True)
            internet = scrapper_instance.get('https://whatismyipaddress.com/')
            self.assertNotEqual(tor_response.find_element_by_class_name("ip-address").text, internet.find_element_by_class_name("ip-address").text)

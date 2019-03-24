import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


class Request:
    def __init__(self, base_url):
        self._capabilities = webdriver.DesiredCapabilities().FIREFOX
        self._capabilities["marionette"] = True
        self._gecko_binary = os.path.join(os.curdir, 'firefox/geckodriver')
        self._firefox_binary = FirefoxBinary(r'/usr/local/bin/firefox')
        self._base_url = base_url
        self._options = Options()
        self._options.headless = True
        self._driver = webdriver.Firefox(capabilities=self._capabilities,
                                         firefox_options=self._options)

    def _fetch_data(self, forecast, area):
        url = self._base_url.format(forecast=forecast, area=area)
        self._driver.get(url)
        if self._driver.title == '404 Not Found':
            error = "Could not find the area that you're searching"
            raise Exception(error)
        return self._driver.page_source

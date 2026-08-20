from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class WebdriverFactory:
    @staticmethod
    def getWebdriver(browserName: str):
        if browserName == "firefox":
            options = FirefoxOptions()
            options.add_argument("-headless")
            return webdriver.Firefox(options=options)

        if browserName == "chrome":
            options = ChromeOptions()
            options.add_argument("--headless=new")
            return webdriver.Chrome(options=options)

        raise ValueError(f"Unsupported browser: {browserName}")

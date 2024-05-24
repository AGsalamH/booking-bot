'''
Booking.com Webdriver that interactes with the webpages.
'''
from types import TracebackType
from typing import Type
from selenium import webdriver
from booking import constants as const


class Booking(webdriver.Chrome):
    '''Booking.com webdriver that controls webpages.'''

    def __init__(self, driver_path: str | None = None, teardown: bool = False):
        self.driver_path = driver_path if driver_path else const.DRIVER_PATH
        self.teardown = teardown
        super().__init__(service=webdriver.ChromeService(self.driver_path))

    def __exit__(self, exc_type, exc, traceback):
        '''Close the browser and shutdown chromedriver.'''
        if self.teardown:
            self.quit()

    def land_homepage(self):
        '''Load booking.com page in the current tab'''
        self.get(const.BASE_URL)

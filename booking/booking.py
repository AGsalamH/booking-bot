'''
Booking.com Webdriver that interactes with the webpages.
'''
from selenium import webdriver
from booking import constants as const


class Booking(webdriver.Chrome):
    '''Booking.com webdriver that controls webpages.'''

    def __init__(self, driver_path: str | None = None):
        self.driver_path = driver_path if driver_path else const.DRIVER_PATH
        super().__init__(service=webdriver.ChromeService(self.driver_path))

    def land_homepage(self):
        '''Load booking.com page in the current tab'''
        self.get(const.BASE_URL)

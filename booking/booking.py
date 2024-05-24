'''
Booking.com Webdriver that interactes with the webpages.
'''

from selenium import webdriver

from booking import constants as const
from booking.locators import HomepageLocators


class Booking(webdriver.Chrome):
    '''Booking.com webdriver that controls webpages.'''

    def __init__(self, driver_path: str | None = None, teardown: bool = False):
        self.driver_path = driver_path if driver_path else const.DRIVER_PATH
        self.teardown = teardown
        super().__init__(service=webdriver.ChromeService(self.driver_path))
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        '''Close the browser and shutdown chromedriver.'''
        if self.teardown:
            self.quit()

    def land_homepage(self):
        '''Load booking.com page in the current tab'''
        self.get(const.BASE_URL)

    def currency_picker(self):
        '''Find and return currency picker button.'''
        return self.find_element(*HomepageLocators.CURRENCY_PICKER)

    def currency_btn(self, currency: str):
        '''
        Find and return specific currency button. \n
        Returns first currency in the list if it can't find the specified currency.
        '''
        all_currencies = self.find_elements(*HomepageLocators.CURRENCY_BTN)

        for currency_element in all_currencies:
            if currency_element.text.upper() == currency.upper():
                return currency_element

        return all_currencies[0]

    def set_currency(self, currency='EGP'):
        '''Set Currency by: \n
            1. Click on currency picker. \n
            2. Click on the specified currency button. \n

            **default is EGP**.
        '''
        self.currency_picker().click()
        self.currency_btn(currency).click()

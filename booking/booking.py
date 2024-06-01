'''
Booking.com Webdriver that interactes with the webpages.
'''
import time
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def _modal_close_btn(self):
        '''Get close Modal button.'''
        return self.find_element(*HomepageLocators.CLOSE_MODAL_BTN)

    def close_modal(self):
        '''Close the modal that appears once the website loads.'''
        try:
            self._modal_close_btn().click()
        except:
            pass

    def explicitly_close_modal(self):
        '''
        Make first try to close the modal explicitly wait for it to appear. \n
        To avoid waiting the whole implicit wait time.
        '''
        try:
            WebDriverWait(self, 4).until(
                EC.presence_of_element_located(HomepageLocators.CLOSE_MODAL_BTN)
            )
            self._modal_close_btn().click()
        except:
            pass

    def location_input(self):
        '''Find and return destination input.'''
        return self.find_element(*HomepageLocators.LOCATION_INPUT)

    def _first_result_option(self):
        '''Find and return first search result option.'''
        return self.find_element(*HomepageLocators.FIRST_RESULT_OPTION)

    def where_you_going(self, location: str):
        '''Set destination location and select first result that appears.'''
        self.location_input().send_keys(location)
        time.sleep(1)  # Cuz it selects the first result before my result search appears
        self._first_result_option().click()

    def _date_is_valid(self, *dates: date):
        '''Check that dates NOT in the past.'''
        today = date.today()
        return all((_date >= today for _date in dates))

    def date_picker(self, _date: date):
        '''Find and return specific date element.'''
        is_valid = self._date_is_valid(_date)
        locator = HomepageLocators.get_date_picker(str(_date))
        if not is_valid:  # set date to today if date is not VALID.
             locator = HomepageLocators.get_date_picker(str(date.today()))

        return self.find_element(*locator)

    def when_you_going(self, check_in: date, check_out: date):
        '''Set check_in & check_out reservation dates.'''

        self.date_picker(check_in).click()
        self.date_picker(check_out).click()

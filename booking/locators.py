'''
All WebElement instances locators should come here.
'''
from selenium.webdriver.common.by import By


class HomepageLocators:
    '''Booking.com Homepage element locators'''

    CURRENCY_PICKER = (By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
    CURRENCY_BTN = (By.CLASS_NAME, 'ea1163d21f')
    CLOSE_MODAL_BTN = (By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
    LOCATION_INPUT = (By.ID, ':re:')
    FIRST_RESULT_OPTION = (By.ID, 'autocomplete-result-0')

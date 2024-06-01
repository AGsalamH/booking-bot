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
    OCCUPANCY_CONFIG_BTN = (By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
    INCREMENT_ADULTS_BTN = (By.XPATH, '//*[@id=":rf:"]/div/div[1]/div[2]/button[2]')
    INCREMENT_ROOMS_BTN = (By.XPATH, '//*[@id=":rf:"]/div/div[3]/div[2]/button[2]')


    @classmethod
    def get_date_picker(cls, str_date: str):  # str_date = '2024-05-26'
        '''dynamic locator to find date element by date value'''
        return (By.CSS_SELECTOR, f'span[data-date="{str_date}"]')

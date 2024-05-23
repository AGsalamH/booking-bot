import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Google:
    def __init__(self):
        '''Initialize chrome driver'''
        chrome_service = webdriver.ChromeService('./driver/chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome_service)
        self.url = 'https://google.com/'

    def get(self):
        '''Load google.com page in the current tab'''
        self.driver.get(self.url)

    def _get_search_input(self):
        'Find and return search input of google.com'
        search_input_class_name = 'gLFyf'
        return self.driver.find_element(By.CLASS_NAME, search_input_class_name)

    def search(self, text: str):
        '''Write text in search input and hit ENTER.'''
        self._get_search_input().send_keys(text + Keys.RETURN)

    def get_first_result(self):
        '''Find and return first result of search.'''
        first_result_title_class_name = 'LC20lb'
        return self.driver.find_element(By.CLASS_NAME, first_result_title_class_name)

    # -------------------- driver related methods ---------------------------
    def set_implicitly_wait(self, time_in_secs: float):
        '''Set time to implicitly wait when trying to get an element.'''
        self.driver.implicitly_wait(time_in_secs)

    def quit(self):
        'Close the browser.'
        self.driver.quit()


if __name__ == '__main__':
    google = Google()

    google.get()
    google.set_implicitly_wait(10)
    google.search('Selenium')
    first_result = google.get_first_result()
    first_result.click()

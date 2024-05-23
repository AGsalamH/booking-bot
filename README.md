
# Selenium
Getting started with Testing and Automating using Selenium.

- Automates browsers *(As if a real user is operating the browser)*
- Test web apps
- Scrape data from websites
- Online bots

---

### **Installation**

- Pretty straight forward
    
    `pip install selenium`
    

---

### **Webdriver**

- Drives a browser natively (Programming interface)
- Implementation of a browser controlling code.

💡 **Selenium provides a dedicated webdriver for each browser**

⚠️ **We need to download a driver executable that’s compatible with the existing browser version**

- After downloading the right browser driver we can either
    - add it’s path to PATH env variable
        - Eg: `os.environ['PATH'] += ['path/to/driver/executable']`
    - Or
        
        ```python
        from selenium import webdriver
        
        # Create chrome service
        chrome_service = webdriver.ChromeService('/path/to/browser/driver')
        
        # pass service to the driver
        driver = webdriver.Chrome(service=chrome_service)
        ```
        

---

### Waits - Implicit & Explicit

### Implicit
- `driver.implicitly_wait(time_in_seconds)`
- This tells driver that if it can't find the element, wait that specified `time_in_seconds` before raising an error.
- Implicit wait is set for the life of the WebDriver object

### Explicit
- Tells the driver to wait for a certain condition before proceeding further in the code
```python 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# This will wait maximum 10 seconds.
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myDynamicElement"))
)

```
💡 **By default, WebDriverWait calls the ExpectedCondition every 500 milliseconds until it returns success**

---

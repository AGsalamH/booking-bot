
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

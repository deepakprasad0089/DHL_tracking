from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException

import time



def trackingFunc(tracking_number):
    order_status=""
    # Automatically handles location of  executable path of chromedriver 
    service = Service(ChromeDriverManager().install())  


    # browser options like incognito, user agent etc.
    chrome_options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
    chrome_options.add_argument('user-agent={0}'.format(user_agent))
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.delete_all_cookies()

    # let the page load before we start
    driver.implicitly_wait(10)

    driver.get("https://www.mydhli.com/global-en/home/tracking.html")
    time.sleep(5)

    # Accept cookies Consent as nothing will get scraped if not done
    e= WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']"))).click()
    time.sleep(2)

    inputTrackingElement= driver.find_element(By.XPATH,"//input[@id='c-tracking--input']")
    inputTrackingElement.send_keys(tracking_number)

    inputTrackingElement.send_keys(Keys.ENTER)

    time.sleep(10)
    try :
        orderStatusElement = driver.find_element(By.XPATH,"//h2[@class='c-tracking-result--status-copy-message level4']")

    except NoSuchElementException:
        orderStatusElement = driver.find_element(By.XPATH,"//span[@class='c-tracking-result-message--content l-grid--left-s']")

    #print(orderStatusElement.text)
    order_status= orderStatusElement.text

    driver.close()

    return order_status

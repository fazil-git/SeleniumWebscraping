from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

PATH = "C:\Program Files (x86)\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#driver.maximize_window()

#* SignUp/Login in a particular website
def dashboard():
    try:
        driver.get("https://www.screener.in/")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://www.screener.in/dash/")
    except:
        driver.get("https://www.screener.in/")
        print("Exception either cookies deleted or dash url expired")

        #* Login, Password and collect cookies
        login = driver.find_element_by_link_text("Login")
        login.click()
        driver.find_element_by_name("username").send_keys("M*****@gmail.com")
        driver.find_element_by_name("password").send_keys("**password**")
        driver.find_element_by_class_name("button-primary").click()
        pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
    
#* Navigating to search bar, enter input and click search to visit next page
dashboard()
search = driver.find_element_by_xpath("/html[1]/body[1]/nav[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
#TODO: Get data from user input
search.send_keys("Reliance Industries Ltd")
time.sleep(1)
search.send_keys(Keys.RETURN)

#* Scraping different data from that page
#print(driver.page_source)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "row-full-width"))
    )
    smain = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "quick-ratios-placeholder"))
    )
    pltable = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/main[1]/div[1]/section[6]/div[3]/table[1]/tbody[1]"))
    )
    print(main.text)
    print(smain.text)
    print(pltable.text)
    

    #TODO: Navigating deep in that site
    """ link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Edit ratios"))
    )
    link.click() """
    
except:
    print("Exception when scraping values")

finally:
    time.sleep(3)
    driver.quit()
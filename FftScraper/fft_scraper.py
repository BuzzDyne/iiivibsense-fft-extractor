from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from constansts import xpaths as Paths

uname = "gimin@iii.co.id"
pw = "eiy0eiqu9Bai"

class FFTScraper:
    def waitForElementToLoad(self, ele):
        if(isinstance(ele, str)):
            self.waitDriver.until(EC.presence_of_element_located((By.XPATH, ele)))

    def navigateToSensorPage(self, uname, pwd):

        self.driver.get("https://iii.vibsense.net/login/")

        def loginPage():
            e = self.driver.find_element_by_name("email")
            e.clear()
            e.send_keys(uname)

            e = self.driver.find_element_by_name("password")
            e.clear()
            e.send_keys(pwd)

            e.send_keys(Keys.RETURN)
            self.waitForElementToLoad(Paths.PAGE_HEADER)

            return self.driver.find_elements_by_xpath(Paths.MENU_ITEMS)

        def menuPage(opts):
            """Recursively navigate to machine page"""
            if(len(opts) == 0):
                # Reached Machine page
                self.waitForElementToLoad(Paths.PAGE_HEADER)
                return

            print("\nPlease choose 1 item from list below:")
            i = 1
            for x in opts:
                print("{} = {}\n".format(i, x.text), end='')
                i += 1

            n = int(input("Input selection number: "))
            n -= 1

            opts[n].click()
            self.waitForElementToLoad(Paths.PAGE_HEADER)

            menuPage(self.driver.find_elements_by_xpath(Paths.MENU_ITEMS))

        def machinePageToSensorPage(sensors):
            print("\nPlease choose 1 item from list below:")
            i = 1
            for x in sensors:
                print("{} = {}\n".format(i, x.text), end='')
                i += 1

            n = int(input("Input selection number: "))
            n -= 1

            sensors[n].click()
            # self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART)

        company_options = loginPage()
        print("Logged in as {}".format(uname))

        menuPage(company_options)

        sensorItems = self.driver.find_elements_by_xpath(Paths.MACHINE_MENU_ITEMS)
        
        machinePageToSensorPage(sensorItems)

        input("x?")
        # for i in range(20):
        #     self.driver.refresh()
        #     self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART)
        #     self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_CHART_CONTAINER).screenshot('{}.png'.format(i))

    def __init__(self, uname, pwd, menuChoices = None):
        self.driver             = webdriver.Chrome()
        self.waitDriver         = WebDriverWait(self.driver,10)
        self.latestTargetTime   = datetime.now()
        self.earliestTargetTime = datetime.now()

        if menuChoices is None:
            # Manual Navigation
            self.navigateToSensorPage(uname, pwd)
        # else:
            # Automatic Navigation

    

        

sc = FFTScraper(uname, pw)
import os

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from constansts import xpaths as Paths
from FftScraper import utils

uname = "gimin@iii.co.id"
pw = "eiy0eiqu9Bai"

dataTargetDir = "data/"

class FFTScraperManual:
    ######### UTIL METHODS #########
    def waitForElementToLoad(self, ele):
        if(isinstance(ele, str)):
            self.waitDriver.until(EC.presence_of_element_located((By.XPATH, ele)))

    def getInputTime(self, timeName, defaultTime):
        inputTime = input("Input {} ('YYYY-MM-DD HH:MM:SS' or just ENTER for default value): ".format(timeName))

        if len(inputTime) == 0:
            time = defaultTime
        else:
            time = utils.convInputStrToDatetime(inputTime)
        
        return time

    ################################

    def sensorPageNextDatarow(self):
        """Go to next DataRow
        
        Only use when on Sensor Page"""

        tableEle = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_DATA_TABLE)
        tableEle.find_elements_by_xpath(Paths.SENSOR_PAGE_DATA_TABLE_ROW)[1].click()
        self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART_CONTAINER)

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
            self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART_CONTAINER)

        company_options = loginPage()
        print("Logged in as {}".format(uname))

        menuPage(company_options)

        sensorItems = self.driver.find_elements_by_xpath(Paths.MACHINE_MENU_ITEMS)        
        machinePageToSensorPage(sensorItems)

        # for i in range(20):
        #     self.driver.refresh()
        #     self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART)
        #     self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_CHART_CONTAINER).screenshot('{}.png'.format(i))

    def navigateToLatestDatarow(self):
        defTime = datetime.now()
        latestTime  = self.getInputTime("latestTime", defTime)

        currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)
        while(currTime > latestTime):
            # Go to next DataRow
            self.sensorPageNextDatarow()
            currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)

    def navigateAndScrapeToEarliestDatarow(self):
        currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)
        defaultTime = currTime - timedelta(days=1)

        sensorNameEle = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_SENSOR_NAME)
        sensorName = str.split(sensorNameEle.text, sep="Vibration data for sensor ")[1]

        earlyTime   = self.getInputTime("earlyTime", defaultTime)

        while currTime > earlyTime:
            # Scrape FFT
            chartEle    = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_CHART_CONTAINER) 
            xyzEle      = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_XYZ)

            # Scroll Down
            self.driver.execute_script("arguments[0].scrollIntoView(true);", xyzEle)

            fileName = utils.convTimeToStr(currTime)

            chartEle.screenshot('{}/{}.png'.format(dataTargetDir, i))

            self.sensorPageNextDatarow()
            self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART_CONTAINER) 
            currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)

    def __init__(self, uname, pwd, jobs = None):
        # Browser Window Size
        opt = webdriver.ChromeOptions()
        opt.add_argument("--window-size=1200,800")

        # Create 'data' dir if doesn't exist
        if not os.path.isdir('data'):
            os.mkdir('data')

        self.driver             = webdriver.Chrome(chrome_options=opt)
        self.waitDriver         = WebDriverWait(self.driver,10)
        self.jobs               = jobs if jobs else None



        # self.driver.get('chrome://settings/')
        # self.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.75);')

        self.navigateToSensorPage(uname, pwd)
        self.navigateToLatestDatarow()
        self.navigateAndScrapeToEarliestDatarow()

        # if self.jobs is None:
            # Manual Navigation
            # self.navigateToSensorPage(uname, pwd)
        # else:
            # Automatic Navigation



        

sc = FFTScraperManual(uname, pw)
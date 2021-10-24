import os

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from constansts import xpaths as Paths
from FftScraper import utils
from FftScraper.job_model import Job

uname = "gimin@iii.co.id"
pw = "eiy0eiqu9Bai"

dataTargetDir = "data/png"

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

    def navigateToSensorPage(self):

        self.driver.get("https://iii.vibsense.net/login/")

        def loginPage():
            e = self.driver.find_element_by_name("email")
            e.clear()
            e.send_keys(uname)

            e = self.driver.find_element_by_name("password")
            e.clear()
            e.send_keys(pw)

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

        # Get Sensor Name
        sensorNameEle = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_SENSOR_NAME)
        sensorName = str.split(sensorNameEle.text, sep="Vibration data for sensor ")[1]
        sensorName = utils.cleanseStr(sensorName)

        # Request EarliestTime from User
        earlyTime   = self.getInputTime("earlyTime", defaultTime)

        while currTime > earlyTime:
            # Scrape FFT
            chartEle    = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_CHART_CONTAINER) 
            xyzEle      = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_XYZ)

            # Scroll Down (or else the screenshot will be cut)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", xyzEle)

            fileName = utils.convTimeToStr(currTime)

            dirName = "{}/{}".format(dataTargetDir,sensorName)
            utils.safeCreateDir(dirName)
            
            chartEle.screenshot('{}/{}.png'.format(dirName, fileName))

            self.sensorPageNextDatarow()
            self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART_CONTAINER) 
            currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)

    def __init__(self):
        # Browser Window Size
        opt = webdriver.ChromeOptions()
        opt.add_argument("--window-size=1200,800")

        # Create 'data' dir if doesn't exist
        utils.safeCreateDir(dataTargetDir)

        self.driver             = webdriver.Chrome(chrome_options=opt)
        self.waitDriver         = WebDriverWait(self.driver,10)

        self.navigateToSensorPage(uname, pw)
        self.navigateToLatestDatarow()
        self.navigateAndScrapeToEarliestDatarow()

class FFTScraper:
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

    def navigateToMachinePage(self):
        self.driver.get("https://iii.vibsense.net/login/")

        def loginPage():
            e = self.driver.find_element_by_name("email")
            e.clear()
            e.send_keys(uname)

            e = self.driver.find_element_by_name("password")
            e.clear()
            e.send_keys(pw)

            e.send_keys(Keys.RETURN)
            self.waitForElementToLoad(Paths.PAGE_HEADER)

            return self.driver.find_elements_by_xpath(Paths.MENU_ITEMS)

        def menuPage(opts, choice):
            """Click one of current page option and return the options of the next page"""
            choice = choice - 1

            choiceName = opts[choice].text

            opts[choice].click()
            print("Selected {}\n".format(choiceName), end='')

            self.waitForElementToLoad(Paths.PAGE_HEADER)

            return self.driver.find_elements_by_xpath(Paths.MENU_ITEMS)

        opts = loginPage()
        print("Logged in as {}".format(uname))

        menuChoices = [self.job.nCompany, self.job.nFactory, self.job.nProdLine, self.job.nMachine]

        for choice in menuChoices:
            opts = menuPage(opts, choice)

    def scrapeSensorData(self):
        def processTsRows(latestTime, tsElements):
            for ts in tsElements:
                currTime = utils.convWebTimeStrToDatetime(ts.text)
                if(currTime <= latestTime):
                    return ts
            
            return tsElements[len(tsElements)-1]


        def navigateToLatestDatarow():
            latestTime  = self.job.latestTime

            currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)
            while(currTime > latestTime):
                # Go to next DataRow
                self.sensorPageNextDatarow()
                currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)

        def navigateToLatestDatarowV2():
            latestTime = self.job.latestTime

            currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)
            
            while(currTime > latestTime):
                tsElements = self.driver.find_elements_by_xpath(Paths.SENSOR_PAGE_TIMESTAMPS)

                resEle = processTsRows(latestTime, tsElements)
                resEle.click()
                self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART_CONTAINER)

                currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)


        def navigateAndScrapeToEarliestDatarow():
            currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)

            # Get Sensor Name
            sensorNameEle = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_SENSOR_NAME)
            sensorName = str.split(sensorNameEle.text, sep="Vibration data for sensor ")[1]
            sensorName = utils.cleanseStr(sensorName)
            print(f'Scraping {sensorName}', end='')

            earlyTime   = self.job.earlyTime
            counter = 0

            while currTime > earlyTime:
                chartEle    = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_CHART_CONTAINER) 
                xyzEle      = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_XYZ)
                faultEle    = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_FAULTS_CONTAINER)

                fileName = utils.convTimeToStr(currTime)
                dirName = f"{dataTargetDir}/{sensorName}"
                utils.safeCreateDir(dirName)

                # Scrape Faults box
                faultEle.screenshot(f'{dirName}/{fileName}_0_faults.png')

                # Scrape FFT Chart
                #       Scroll Down (or else the screenshot will be cut)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", xyzEle)
                chartEle.screenshot(f'{dirName}/{fileName}.png')

                print('.', end='')
                counter = counter + 1

                self.sensorPageNextDatarow()
                self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART_CONTAINER) 
                currTime = utils.convWebTimeStrToDatetime(self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text)

            print(f' ({counter})\n', end='')

        # Inside MachinePage
        sensorItems = self.driver.find_elements_by_xpath(Paths.MACHINE_MENU_ITEMS)
        sensorLinks = []
        selectedIndexes = []

        for i in sensorItems:
            sensorLinks.append(i.get_attribute('href'))

        # Selected Sensors
        if (len(self.job.nSensor) == 0):
            selectedIndexes = list(range(len(sensorLinks))) 
        else: 
            selectedIndexes = self.job.nSensor
            selectedIndexes = [x-1 for x in selectedIndexes]

        for i in selectedIndexes:
            self.driver.get(sensorLinks[i])
            self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART_CONTAINER)
            
            # navigateToLatestDatarow()
            # Todo
            navigateToLatestDatarowV2()
            navigateAndScrapeToEarliestDatarow()

    def __init__(self, username, password, job, headless):
        # Browser Window Size
        opt = webdriver.ChromeOptions()
        opt.add_argument("--window-size=1200,800")
        
        if(headless):
            opt.add_argument('--headless')
            opt.headless = True

        # Create 'data' dir if doesn't exist
        utils.safeCreateDir(dataTargetDir)

        self.driver             = webdriver.Chrome(chrome_options=opt)
        self.waitDriver         = WebDriverWait(self.driver,10)
        self.job                = job

        uname = username
        pw = password

        self.navigateToMachinePage()

        self.scrapeSensorData()

        self.driver.quit()

class FFTScraperIndividual:
    ######### UTIL METHODS #########
    def waitForElementToLoad(self, ele):
        if(isinstance(ele, str)):
            self.waitDriver.until(EC.presence_of_element_located((By.XPATH, ele)))

    def login(self):
        print("Logging in", end="")
        self.driver.get("https://iii.vibsense.net/login/")

        e = self.driver.find_element_by_name("email")
        e.clear()
        e.send_keys(uname)

        e = self.driver.find_element_by_name("password")
        e.clear()
        e.send_keys(pw)

        e.send_keys(Keys.RETURN)
        self.waitForElementToLoad(Paths.PAGE_HEADER)
        print("... ", end="")

        # Pick Company
        opts = self.driver.find_elements_by_xpath(Paths.MENU_ITEMS)
        opts[0].click()
        self.waitForElementToLoad(Paths.PAGE_HEADER)
        print("DONE!")

    def scrapePages(self, urls):
        listOfCode = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        def scrapePage(url, code):
            # Go to URL
            self.driver.get(url)
            self.waitForElementToLoad(Paths.SENSOR_PAGE_CHART_CONTAINER)

            # Get Curr Time
            currTimeText = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_TS_ABS).text
            currTime = utils.convWebTimeStrToDatetime(currTimeText)

            # Get Sensor Name
            sensorNameEle = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_SENSOR_NAME)
            sensorName = str.split(sensorNameEle.text, sep="Vibration data for sensor ")[1]
            sensorName = utils.cleanseStr(sensorName)
            print(f'Scraping {sensorName} at {currTime}... ', end='')

            # Start Scraping
            xyzEle      = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_XYZ)

            peakRmsRowEle   = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_PEAKRMS_ROW)
            graphRowEle     = self.driver.find_element_by_xpath(Paths.SENSOR_PAGE_GRAPH_ROW)

            fileName = utils.convTimeToMonthYearStr(currTime)
            dirName = f"{dataTargetDir}/{sensorName}"
            utils.safeCreateDir(dirName)

            # Scrape First Row
            peakRmsRowEle.screenshot(f'{dirName}/{fileName}_{code}_rms.png')

            # Scrape FFT Row
            #       Scroll Down (or else the screenshot will be cut, not needed if headless)
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", xyzEle)
            graphRowEle.screenshot(f'{dirName}/{fileName}_{code}_fft.png')

            print('DONE!')
        
        i = 0
        for url in urls:
            scrapePage(url, listOfCode[i])
            i+=1

    def __init__(self, urls, username=uname, password=pw, headless=False):
        # Browser Window Size
        opt = webdriver.ChromeOptions()
        opt.add_argument("--window-size=1200,800")
        
        if(headless):
            opt.add_argument('--headless')
            opt.headless = True

        # Create 'data' dir if doesn't exist
        utils.safeCreateDir(dataTargetDir)
        self.driver             = webdriver.Chrome(chrome_options=opt)
        self.waitDriver         = WebDriverWait(self.driver,10)

        self.login()
        self.scrapePages(urls)








# sc = FFTScraperManual(uname, pw)
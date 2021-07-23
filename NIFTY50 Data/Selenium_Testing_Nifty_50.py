from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# To get the csv file which contains the data of NIFTY50 company names
def getNIFTY50Companies():
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://en.wikipedia.org/wiki/NIFTY_50")
    driver.implicitly_wait(10)

    tableExcel=[]

    print(driver.title)

    try:
        table = driver.find_element_by_id("constituents")

        columnHead = table.find_elements_by_class_name("headerSort")

        # For Table Headers
        tableHeaders = []

        for th in columnHead:
            tableHeaders.append(th.text)

        # For Table Data
        tableData = []
        tableBodyData = table.find_elements_by_tag_name("td")

        # print(len(tableBodyData)/3)

        for i in range(int(len(tableBodyData)/3)):
            for j in range(3):
                dataToBeAdded = tableBodyData[3*i+j].text
                # To remove .NS 
                if(j==1):
                    dataToBeAdded = dataToBeAdded.split(".")[0]
                tableData.append(dataToBeAdded)
            tableExcel.append(tableData)
            tableData=[]        
        
        df = pd.DataFrame(tableExcel,columns=[tableHeaders[0],tableHeaders[1],tableHeaders[2]])

        df.to_csv("NIFTY50Companies.csv",index=False)

    except:
        print("Not Working")
        time.sleep(4)

    driver.quit()

# To get the csv file which contains the data of NIFTY50 Annual Returns
def getNIFTY50AnnualReturns():
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://en.wikipedia.org/wiki/NIFTY_50")
    driver.implicitly_wait(10)

    tableExcel=[]

    print(driver.title)

    try:
        table = driver.find_element_by_xpath("//*[@id=\"mw-content-text\"]/div[1]/table[6]")

        columnHead = table.find_elements_by_class_name("headerSort")

        # For Table Headers
        tableHeaders = []

        for th in columnHead:
            headers = th.text.replace("\n"," ")
            tableHeaders.append(headers)

        # For Table Data
        tableData = []
        tableBodyData = table.find_elements_by_tag_name("td")

        for i in range(int(len(tableBodyData)/4)):
            for j in range(4):
                dataToBeAdded = tableBodyData[4*i+j].text
                tableData.append(dataToBeAdded)
            tableExcel.append(tableData)
            tableData=[] 

        df = pd.DataFrame(tableExcel,columns=[tableHeaders[0],tableHeaders[1],tableHeaders[2],tableHeaders[3]])

        df.to_csv("NIFTY50AnnualReturns.csv",index=False)

    except:
        print("Not Working")
        time.sleep(4)

    driver.quit()

if(__name__ == "__main__"):
    getNIFTY50Companies()
    getNIFTY50AnnualReturns()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def getWeatherData(name):
    PATH = "chromedriver.exe"
    # Initliazing the Webdriver
    driver = webdriver.Chrome(PATH)

    driver.get("https://wea-app.netlify.app")
    driver.implicitly_wait(10)
    
    print("\n"+driver.title+"\n")


    # weather = driver.find_element_by_link_text("Weather")
    weather = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Weather")))
    weather.click()

    try:
        cityName = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"cityName")))
        cityName.send_keys(name)
        cityName.send_keys(Keys.RETURN)

        time.sleep(2)

        # cityInfo = WebdriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"article")))
        
        cityInfo = driver.find_elements_by_tag_name("article")

        for cityinfo in cityInfo:
            infoHeading = cityinfo.find_elements_by_tag_name("h2")
            print(infoHeading[0].text)

            infoPara = cityinfo.find_elements_by_tag_name("p")
            for infopara in infoPara:
                print(infopara.text)   

            print()         

    except:
        print("Exiting the program")
        driver.quit()

# Running out program
if __name__=="__main__":
    cityNameUser = input("Enter the name of city whose weather details you want to find:- ")
    getWeatherData(cityNameUser)


__author__ = 'Karan.Patel'

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#location of the chromedriver
webdriver = webdriver.Chrome("C:\Users\Karan\Downloads\chromedriver_win32(2019)\chromedriver.exe")

webdriver.get("https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem")
webdriver.get_screenshot_as_file("addCourse.png")
login = webdriver.find_element_by_name("loginform")
userElement = login.find_element_by_id("mli")
passElement = login.find_element_by_id("password")
loginButtonElement = webdriver.find_element_by_name("dologin")
#This is where you input your yorku passport username
userElement.send_keys("USER")
#This iswhere you input your yorku passport password
passElement.send_keys("PASS")


loginButtonElement.click()

webdriver.get_screenshot_as_file("confirmation.png")
WebDriverWait(webdriver,10).until(EC.title_contains("REM - Main"))
webdriver.get_screenshot_as_file("enrollmentPage.png")
selection = webdriver.find_element_by_tag_name("select")
selection.click()
allOptions = selection.find_elements_by_tag_name("option")
for option in allOptions:
    print "Option is:" + option.get_attribute("value")
    # at this time option 1 = enroll in Fall2019/Winter2020
    # the options might change over time
    if (option.get_attribute("value") == '1'):
        option.click()

webdriver.get_screenshot_as_file("optionSelected.png")
webdriver.quit()

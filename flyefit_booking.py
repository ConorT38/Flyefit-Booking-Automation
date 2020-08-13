import time
import enum
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  

class TimeSlot:
    _5_30 = 0
    _7_00 = 1
    _8_30 = 2
    _10_00 = 3
    _11_30 = 4
    _13_00 = 5
    _14_30 = 6
    _16_00 = 7
    _17_30 = 8
    _19_00 = 9
    _20_30 = 10
    _22_00 = 11

chrome_options = Options()  
chrome_options.add_argument("--headless")  

# Enter user preferences here:
########################
EMAIL = ""
PASSWORD = ""
TIMESLOT = TimeSlot._7_00
########################

today = str(datetime.date.today() + datetime.timedelta(days=1))

driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('https://myflye.flyefit.ie/login')

email_box = driver.find_element_by_name('email_address')
email_box.send_keys(EMAIL)

password_box = driver.find_element_by_name('password')
password_box.send_keys(PASSWORD)

login_button = driver.find_element_by_name('log_in')
login_button.click()

driver.get('https://myflye.flyefit.ie/myflye/book-workout/167/12/'+today)
booking_slot = driver.find_elements_by_class_name("btn-primary")
booking_slot[TIMESLOT].click()

book_button = driver.find_element_by_name('book_class')
driver.execute_script("arguments[0].click();", book_button)

time.sleep(3)
driver.quit()
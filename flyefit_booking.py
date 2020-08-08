import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


EMAIL = ""
PASSWORD = ""
today = str(datetime.date.today() + datetime.timedelta(days=1))

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://myflye.flyefit.ie/login')

email_box = driver.find_element_by_name('email_address')
email_box.send_keys(EMAIL)

password_box = driver.find_element_by_name('password')
password_box.send_keys(PASSWORD)

login_button = driver.find_element_by_name('log_in')
login_button.click()

driver.get('https://myflye.flyefit.ie/myflye/book-workout/167/12/'+today)
booking_slot = driver.find_element_by_class_name("btn-primary")
booking_slot.click()

book_button = driver.find_element_by_name('book_class')
driver.execute_script("arguments[0].click();", book_button)

time.sleep(5)
driver.quit()
from selenium import webdriver
from getpass import getpass #for password security.
from webdriver_manager.chrome import ChromeDriverManager
usr=input('enter email/number: ')
pwd=getpass('enter password: ')
browser=webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.facebook.com")

usernam=browser.find_element_by_id("email")
usernam.send_keys(usr)
passwor=browser.find_element_by_id("pass")
passwor.send_keys(pwd)
logi=browser.find_element_by_xpath("//input[starts-with(@id,'u_0')]")
logi.submit()
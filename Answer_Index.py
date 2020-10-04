from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
import re
import json


f_name_list=['JEE-Mains-2017-Paper-1-2nd-April','JEE-Mains-2018-Paper-1-8th-April','JEE-Mains-2018-Paper-1-15th-April','JEE-Mains-2018-Paper-1-16th-April','JEE-Mains-2019-8th-April-Shift-2','JEE-Mains-2019-10th-April-Shift-2','JEE-Mains-2019-Paper-1-8th-April-Shift-1','JEE-Mains-2019-Paper-1-9th-April-Shift-1','JEE-Mains-2019-Paper-1-9th-April-Shift-2','JEE-Mains-2019-Paper-1-9th-Jan-Shift-1','JEE-Mains-2019-Paper-1-9th-Jan-Shift-2','JEE-Mains-2019-Paper-1-10th-April-Shift-1','JEE-Mains-2019-Paper-1-12th-April-Shift-1','JEE-Mains-2019-Paper-1-12th-April-Shift-2']
base_url='localhost:8000/compete/'
j=1

for thing in f_name_list:
    thing2=thing.lower()
    driver = webdriver.Chrome('chromedriver.exe')
    f_url=base_url+"addoptions?"+"cname="+str(thing2)+"&"+"fname="+str(thing2)
    driver.get(f_url)
    time.sleep(10)
    print(thing2 + "Done!" + str(j))
    driver.close()
    driver.quit()

print("All Done")
    
    
    
    

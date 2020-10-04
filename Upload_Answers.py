from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
import re
import json


f_name_list=['JEE-Mains-2013-Paper-1-7th-April','JEE-Mains-2014-11th-April','JEE-Mains-2014-19th-April','JEE-Mains-2014-Paper-1-6th-April-1','JEE-Mains-2014-Paper-1-9th-April','JEE-Mains-2015-10th-April','JEE-Mains-2015-Paper-1-4th-April','JEE-Mains-2015-Paper-1-11th-April','JEE-Mains-2016-3rd-April','JEE-Mains-2016-10th-April','JEE-Mains-2017-9th-April','JEE-Mains-2017-Paper-1-2nd-April','JEE-Mains-2017-Paper-1-8th-April','JEE-Mains-2018-Paper-1-8th-April','JEE-Mains-2018-Paper-1-15th-April','JEE-Mains-2018-Paper-1-16th-April','JEE-Mains-2019-8th-April-Shift-2','JEE-Mains-2019-10th-April-Shift-2','JEE-Mains-2019-10th-Jan-Shift-1','JEE-Mains-2019-10th-Jan-Shift-2','JEE-Mains-2019-11th-Jan-Shift-1','JEE-Mains-2019-Paper-1-8th-April-Shift-1','JEE-Mains-2019-Paper-1-9th-April-Shift-1','JEE-Mains-2019-Paper-1-9th-April-Shift-2','JEE-Mains-2019-Paper-1-9th-Jan-Shift-1','JEE-Mains-2019-Paper-1-9th-Jan-Shift-2','JEE-Mains-2019-Paper-1-10th-April-Shift-1','JEE-Mains-2019-Paper-1-12th-April-Shift-1','JEE-Mains-2019-Paper-1-12th-April-Shift-2','JEE-Mains-2019-Paper-1-12th-Jan-Shift-1','JEE-Mains-2019-Paper-1-12th-Jan-Shift-2','JEE-Mains-2020-7th-Jan-Shift-1','JEE-Mains-2020-7th-Jan-Shift-2','JEE-Mains-2020-8th-Jan-Shift-1','JEE-Mains-2020-8th-Jan-Shift-2','JEE-Mains-2020-9th-Jan-Shift-1','JEE-Mains-2020-9th-Jan-Shift-2']

base_url='localhost:8000/compete/'
j=1

for thing in f_name_list:
    driver = webdriver.Chrome('chromedriver.exe')
    f_url=base_url+"addquestions?"+"cname="+str(thing)+"&"+"fname="+str(thing)
    driver.get(f_url)
    time.sleep(20)
    print(thing + "Done!" + str(j))
    driver.close()
    driver.quit()

print("All Done")
    
    
    
    

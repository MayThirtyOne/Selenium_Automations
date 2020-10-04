from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

from PIL import Image
from io import BytesIO
from io import StringIO
import re
import json





driver = webdriver.Chrome('chromedriver.exe')


driver.get('https://www.embibe.com/mock-test/jee-main/chemistry/part-test-4-organic-chemistry-part-test-1/session')

for k in range(10):
    print(k)
    time.sleep(1)




elements = driver.find_elements_by_class_name("btn-container")
elements[1].click()
driver.maximize_window()

with open("QBJSONCHEM.json", 'a', encoding='utf-8') as f:
    print("[\n",file=f)
    

for i in range(1,90,1):
    time.sleep(3)
    var5=driver.find_elements_by_class_name("-body")
    var6=var5[0].get_attribute('innerHTML')
    var7=var6.strip()
    var8=str(var7)
    var10=driver.find_elements_by_class_name("__name ")
    var13=driver.find_elements_by_class_name("__text")
    print(len(var10), len(var13))
    optionname1=(var10[0].get_attribute('innerHTML')).strip()
    optionname2=(var10[1].get_attribute('innerHTML')).strip()
    optionname3=(var10[2].get_attribute('innerHTML')).strip()
    optionname4=(var10[3].get_attribute('innerHTML')).strip()
    optionvalue1=(var13[0].get_attribute('innerHTML')).strip()
    optionvalue2=(var13[1].get_attribute('innerHTML')).strip()
    optionvalue3=(var13[2].get_attribute('innerHTML')).strip()
    optionvalue4=(var13[3].get_attribute('innerHTML')).strip()
    optionvalue1=re.sub('<span class="MJX_Assistive_MathML".*?</math></span>', '', optionvalue1)
    optionvalue2=re.sub('<span class="MJX_Assistive_MathML".*?</math></span>', '', optionvalue2)
    optionvalue3=re.sub('<span class="MJX_Assistive_MathML".*?</math></span>', '', optionvalue3)
    optionvalue4=re.sub('<span class="MJX_Assistive_MathML".*?</math></span>', '', optionvalue4)
    
    
    

    
    
    var8=re.sub('<span class="MJX_Assistive_MathML".*?</math></span>', '', var8)
    #print(var8)
    dict1={}
    dict1["question"]=var8.strip()
    dict1["option1"]=optionvalue1.strip()
    dict1["option2"]=optionvalue2.strip()
    dict1["option3"]=optionvalue3.strip()
    dict1["option4"]=optionvalue4.strip()
    
    with open("QBJSON.json", 'a', encoding='utf-8') as f:
        json.dump(dict1, f, indent = 4, sort_keys = False)
        print("\n,\n",file=f)
        print(str(i)+" done")
        
    #var2=driver.find_elements_by_class_name("button-skip-box")
    #var2[0].click()
    time.sleep(5)
    var3=driver.find_elements_by_class_name("button-save-n-next-box")
    var3[0].click()
    time.sleep(2)

with open("QBJSON.json", 'a', encoding='utf-8') as f:
    print("]\n",file=f)

print("All Done")



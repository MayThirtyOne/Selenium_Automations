from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
import re
import json



url='https://www.embibe.com/mock-test/jee-main/previous-year-papers/2016-paper-1-9th-april/session'

file_name=str(re.search(r'papers/(.*?)/session', url).group(1))

driver = webdriver.Chrome('chromedriver.exe')


driver.get(url)

for k in range(10):
    print(k)
    time.sleep(1)




elements = driver.find_elements_by_class_name("btn-container")
elements[1].click()
driver.maximize_window()
time.sleep(10)

with open(file_name+".json", 'a', encoding='utf-8') as f:
    print("[\n",file=f)
    

for i in range(1,91,1):
    time.sleep(2)
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
    
    with open(file_name+".json", 'a', encoding='utf-8') as f:
        json.dump(dict1, f, indent = 4, sort_keys = False)
        print("\n,\n",file=f)
        print(str(i)+" done")
        
    #var2=driver.find_elements_by_class_name("button-skip-box")
    #var2[0].click()
    #time.sleep(5)
    var3=driver.find_elements_by_class_name("button-save-n-next-box")
    var3[0].click()
    time.sleep(1)

with open(file_name+".json", 'a', encoding='utf-8') as f:
    print("]\n",file=f)

print("All Done")



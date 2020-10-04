from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
import random
import string
import threading




def gen_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def login_logout_cycle(user,password_1):
    driver.get('https://sphererank.com/logout/')
    driver.get('https://sphererank.com/login/')
    username = driver.find_element_by_id("id_username")
    password = driver.find_element_by_id("id_password")
    username.send_keys(user)
    password.send_keys(password_1)
    driver.find_element_by_xpath('//button[text()="Submit"]').click()
    time.sleep(1)





def register_first_time(user,email_address,password):
    driver.get('https://sphererank.com/register/')
    time.sleep(1)
    username = driver.find_element_by_id("id_username")
    email = driver.find_element_by_id("id_email")
    password1 = driver.find_element_by_id("id_password1")
    password2 = driver.find_element_by_id("id_password2")
    password1.send_keys(password)
    password2.send_keys(password)
    username.send_keys(user)
    email.send_keys(email_address)
    driver.find_element_by_xpath('//button[text()="Submit"]').click()
    time.sleep(1)
    
    

def random_visit_url():
    url_list=['https://sphererank.com/','https://sphererank.com/compete/','https://sphererank.com/previous?type=JEE%20Advanced','https://sphererank.com/previous?type=Others','https://sphererank.com/account/','https://sphererank.com/mycoins/','https://sphererank.com/myteams/','https://sphererank.com/profile/Admin']
    random_url=random.choice(url_list)
    driver.get(random_url)
    time.sleep(1)


def main():
    user="automated_testting_user_"+gen_string(4)
    email_address=gen_string(5)+"@"+gen_string(4)+".com"
    password=gen_string(10)
    register_first_time(user,email_address,password)
    random_visit_url()
    login_logout_cycle(user,password)

    

    
if __name__ == "__main__":
    total_threads=2
    thread_list = list()
    for i in range(total_threads):
        driver = webdriver.Chrome('chromedriver.exe')
        t = threading.Thread(name='Test {}'.format(i), target=main)
        t.start()
        time.sleep(1)
        print( t.name + ' started!')
        thread_list.append(t)
        
    for thread in thread_list:
        thread.join()
    print ('Test completed!')
        
        

    

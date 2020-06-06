from selenium import webdriver
import mysql.connector
import time

executable_path = "/home/grow/Documents/Diplom/Pars_eShop/chromedriver"
chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=executable_path)

driver.get('https://www.itbox.ua/product/Monitor_LG_19M38A-B-p214247/')
try:
    itbox_com_count = driver.find_element_by_class_name("header-comments-count").text.split(" ")[0]
except:
    itbox_com_count = 0
print(itbox_com_count)

driver.get('https://rozetka.com.ua/lenovo_81mx002rra/p172194373/')
try:
    rozetka_com_count = driver.find_element_by_class_name("product-tabs__link-text").text
except:
    rozetka_com_count = 0
print(rozetka_com_count)

driver.get('https://www.citrus.ua/noutbuki-i-ultrabuki/apple-macbook-air-13256-space-gray-2020-663765.html')
try:
    citrus_com_count = driver.find_elements_by_class_name("el-tabs__item")[3].text.split(" ")[1]
except:
    citrus_com_count = 0
print(citrus_com_count)

driver.get('https://allo.ua/ru/products/notebooks/apple-a1466-macbook-air-mqd32ua-a.html')
try:
    allo_com_count = driver.find_element_by_xpath("//a[@id='discussionTab']").text.split(" ")[-1]
except:
    allo_com_count = 0
print(allo_com_count)

driver.get('https://stylus.ua/apple-macbook-air-13-mqd32-2017-p294159c168.html')
try:
    driver.maximize_window()
    stylus_com_count = driver.find_element_by_class_name("count-of-reviews").text.split(" ")[0]
except:
    stylus_com_count = 0
print(stylus_com_count)
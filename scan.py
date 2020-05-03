from selenium import webdriver
import mysql.connector
import time


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="eShop"
)
cursor = mydb.cursor()


executable_path = "/home/grow/Documents/Diplom/Pars_eShop/chromedriver"
chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=executable_path)


def cycle(id):
    print(id)
    query = "select count(id) from FoxApp_contributor;"
    cursor.execute(query)
    counter = cursor.fetchone()
    while id <= counter[0]:
        query = "select category_id from FoxApp_contributor where id = '" + str(id) + "';"
        cursor.execute(query)
        type_ = cursor.fetchone()
        try:
            if type_[0] == 1:
                pc(id)
            elif type_[0] == 2:
                laptop(id)
            elif type_[0] == 3:
                smartphone(id)
        except:
            id = id + 1
            cycle(id)
        id = id + 1

def pc(id):
    id = "'"+str(id)+"'"
    query = "select link_itbox, link_rozetka, link_citrus, link_allo, link_stylus  from FoxApp_contributor where id = "+id+";"
    cursor.execute(query)
    link = cursor.fetchone()
    itbox = link[0]
    rozetka = link[1]
    citrus = link[2]
    allo = link[3]
    stylus = link[4]
    driver.get(itbox)
    driver.find_element_by_class_name("characteristic-toggle").click()
    elements1 = []
    info = driver.find_elements_by_tag_name("td")
    for elem in info:
        elements1.append(elem.text)
    i = 0
    for elem in elements1:
        i = i+1
        if elem == "Серия процессора":
            cpu = elements1[i]
        if elem == "Частота процессора, ГГц":
            speed = elements1[i]
        if elem == "Модель видеокарты":
            videocard = elements1[i]
        if elem == "Тип памяти":
            ram_type = elements1[i]
        if elem == "Объем установленной памяти":
            ram = elements1[i].split("ГБ")[0]
        if elem == "Типы внутренних накопителей":
            hd_type = elements1[i]
        if elem == "Объем HDD" or elem == "Объем SSD":
            hd = elements1[i].split(" ")[0]
    try:
        itbox_price = driver.find_element_by_class_name("stuff-price").text.split("грн")[0].replace(' ', '')
        itbox_price = int(itbox_price)
    except:
        itbox_price = 0
    try:
        driver.get(rozetka)
        driver.implicitly_wait(5)
        rozetka_price = driver.find_element_by_class_name("product-prices__big").text.split("₴")[0].replace(' ', '')
        rozetka_price = int(rozetka_price)
    except:
        rozetka_price = 0
    try:
        driver.get(citrus)
        time.sleep(1)
        driver.implicitly_wait(5)
        citrus_price = driver.find_element_by_xpath("//div[@class='price']").text.split("₴")[0].replace(' ', '')
        citrus_price = int(citrus_price)
    except:
        citrus_price = 0
    try:
        driver.get(allo)
        driver.implicitly_wait(5)
        allo_price = driver.find_element_by_xpath("//meta[@itemprop='price']").get_attribute("content").replace(' ', '')
        allo_price = int(allo_price)
    except:
        allo_price = 0
    try:
        driver.get(stylus)
        driver.implicitly_wait(5)
        stylus_price = driver.find_element_by_class_name("regular-price").text.split("грн")[0].replace(' ', '')
        stylus_price = int(stylus_price)
    except:
        stylus_price = 0
    if int(hd) < 10:
        hd = int(hd)*1000
    category_id = 1
    print(id.split("'")[1], cpu, speed, videocard, ram_type, ram, hd_type, hd, itbox_price, rozetka_price, citrus_price, allo_price,
          stylus_price, category_id)
    sql = "INSERT INTO FoxApp_products (id, cpu, speed, videocard, ram_type, ram, hd_type, hd, price_itbox, price_rozetka, " \
          "price_citrus, price_allo, price_stylus, category_id, model_id) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id.split("'")[1], cpu, speed, videocard, ram_type, ram, hd_type, hd, itbox_price, rozetka_price, citrus_price, allo_price, stylus_price, category_id, id.split("'")[1])
    cursor.execute(sql, val)
    mydb.commit()




def laptop(id):
    id = "'" + str(id) + "'"
    query = "select link_itbox, link_rozetka, link_citrus, link_allo, link_stylus  from FoxApp_contributor where id = " + id + ";"
    cursor.execute(query)
    link = cursor.fetchone()
    itbox = link[0]
    rozetka = link[1]
    citrus = link[2]
    allo = link[3]
    stylus = link[4]
    driver.get(itbox)
    driver.find_element_by_class_name("characteristic-toggle").click()
    elements1 = []
    info = driver.find_elements_by_tag_name("td")
    for elem in info:
        elements1.append(elem.text)
    i = 0
    for elem in elements1:
        i = i + 1
        if elem == "Процессор":
            proc = elements1[i]
            cpu = proc.split("(")[0]
            speed = proc.split("(")[1].replace(')', '').split("ГГц")[0]
        if elem == "Модель видеокарты" or elem == "Видеокарта":
            videocard = elements1[i]
        if elem == "Тип оперативной памяти":
            ram_type = elements1[i]
        if elem == "Объем оперативной памяти":
            ram = elements1[i].split("ГБ")[0]
        if elem == "Типы внутренних накопителей" or elem == "Оптический привод":
            hd_type = elements1[i]
        if elem == "Объем HDD" or elem == "Объем SSD":
            hd = elements1[i].split(" ")[0]
    try:
        itbox_price = driver.find_element_by_class_name("stuff-price").text.split("грн")[0].replace(' ', '')
        itbox_price = int(itbox_price)
    except:
        itbox_price = 0
    try:
        driver.get(rozetka)
        driver.implicitly_wait(5)
        rozetka_price = driver.find_element_by_class_name("product-prices__big").text.split("₴")[0].replace(' ', '')
        rozetka_price = int(rozetka_price)
    except:
        rozetka_price = 0
    try:
        driver.get(citrus)
        time.sleep(1)
        driver.implicitly_wait(5)
        citrus_price = driver.find_element_by_xpath("//div[@class='price']").text.split("₴")[0].replace(' ', '')
        citrus_price = int(citrus_price)
    except:
        citrus_price = 0
    try:
        driver.get(allo)
        driver.implicitly_wait(5)
        allo_price = driver.find_element_by_xpath("//meta[@itemprop='price']").get_attribute("content").replace(' ', '')
        allo_price = int(allo_price)
    except:
        allo_price = 0
    try:
        driver.get(stylus)
        driver.implicitly_wait(5)
        stylus_price = driver.find_element_by_class_name("regular-price").text.split("грн")[0].replace(' ', '')
        stylus_price = int(stylus_price)
    except:
        stylus_price = 0
    if int(hd) < 10:
        hd = int(hd)*1000
    category_id = 2
    print(id.split("'")[1], cpu, float(speed), videocard, ram_type, int(ram), hd_type, hd, itbox_price, rozetka_price, citrus_price, allo_price,
          stylus_price, category_id)
    sql = "INSERT INTO FoxApp_products (id, cpu, speed, videocard, ram_type, ram, hd_type, hd, price_itbox, price_rozetka, " \
          "price_citrus, price_allo, price_stylus, category_id, model_id) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id.split("'")[1], cpu, float(speed), videocard, ram_type, int(ram), hd_type, hd, itbox_price, rozetka_price, citrus_price, allo_price, stylus_price, category_id, id.split("'")[1])
    cursor.execute(sql, val)
    mydb.commit()



def smartphone(id):
    id = "'" + str(id) + "'"
    query = "select link_itbox, link_rozetka, link_citrus, link_allo, link_stylus  from FoxApp_contributor where id = " + id + ";"
    cursor.execute(query)
    link = cursor.fetchone()
    itbox = link[0]
    rozetka = link[1]
    citrus = link[2]
    allo = link[3]
    stylus = link[4]
    driver.get(itbox)
    driver.find_element_by_class_name("characteristic-toggle").click()
    elements1 = []
    info = driver.find_elements_by_tag_name("td")
    for elem in info:
        elements1.append(elem.text)
    i = 0
    for elem in elements1:
        i = i + 1
        if elem == "Диагональ экрана":
            diagonal = elements1[i].split('"')[0]
        if elem == "Процессор":
            cpu = elements1[i]
        if elem == "Оперативная память":
            ram = elements1[i].split("Gb")[0]
        if elem == "Основная камера":
            back_cam = elements1[i]
            main_cam = back_cam.split(" ")[0]
        if elem == "Фронтальная камера":
            front_cam = elements1[i]
        if elem == "Операционная система":
            os = elements1[i]
        if elem == "Цвет":
            color = elements1[i]
    try:
        itbox_price = driver.find_element_by_class_name("stuff-price").text.split("грн")[0].replace(' ', '')
        itbox_price = int(itbox_price)
    except:
        itbox_price = 0
    try:
        driver.get(rozetka)
        driver.implicitly_wait(5)
        rozetka_price = driver.find_element_by_class_name("product-prices__big").text.split("₴")[0].replace(' ', '')
        rozetka_price = int(rozetka_price)
    except:
        rozetka_price = 0
    try:
        driver.get(citrus)
        time.sleep(1)
        driver.implicitly_wait(5)
        citrus_price = driver.find_element_by_xpath("//div[@class='price']").text.split("₴")[0].replace(' ', '')
        citrus_price = int(citrus_price)
    except:
        citrus_price = 0
    try:
        driver.get(allo)
        driver.implicitly_wait(5)
        allo_price = driver.find_element_by_xpath("//meta[@itemprop='price']").get_attribute("content").replace(' ', '')
        allo_price = int(allo_price)
    except:
        allo_price = 0
    try:
        driver.get(stylus)
        driver.implicitly_wait(5)
        stylus_price = driver.find_element_by_class_name("regular-price").text.split("грн")[0].replace(' ', '')
        stylus_price = int(stylus_price)
    except:
        stylus_price = 0
    category_id = 3
    print(id.split("'")[1], cpu, float(diagonal), int(main_cam), back_cam, front_cam, ram, color, os, itbox_price,
           rozetka_price, citrus_price, allo_price, stylus_price, category_id)
    sql = "INSERT INTO FoxApp_products (id, cpu, diagonal, main_cam, back_cam, front_cam, ram, color, os, price_itbox, price_rozetka, " \
          "price_citrus, price_allo, price_stylus, category_id, model_id) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id.split("'")[1], cpu, float(diagonal), int(main_cam), back_cam, front_cam, ram, color, os, itbox_price,
           rozetka_price, citrus_price, allo_price, stylus_price, category_id, id.split("'")[1])
    cursor.execute(sql, val)
    mydb.commit()


if __name__ == '__main__':
    try:
        cycle(1)
    except:
        pass

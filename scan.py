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
    print("asfa")
    print(id)
    query = "select count(id) from contributors;"
    cursor.execute(query)
    counter = cursor.fetchone()
    while id <= counter[0]:
        query = "select type from contributors where id = '" + str(id) + "';"
        cursor.execute(query)
        type_ = cursor.fetchone()
        print(type_[0])
        try:
            if type_[0] == "PC":
                pc(id)
            elif type_[0] == "laptop":
                laptop(id)
            elif type_[0] == "phone":
                smartphone(id)
        except:
            id = id + 1
            cycle(id)
        id = id + 1



def pc(id):
    id = "'"+str(id)+"'"
    query = "select link_itbox, link_rozetka, link_citrus, link_allo, link_stylus  from contributors where id = "+id+";"
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
    print(elements1)
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
    print(cpu, speed, videocard, ram_type, ram, hd_type, hd)
    itbox_price = driver.find_element_by_class_name("stuff-price").text.split("грн")[0]
    print(itbox_price)
    driver.get(rozetka)
    driver.implicitly_wait(5)
    rozetka_price = driver.find_element_by_class_name("product-prices__big").text.split("₴")[0]
    print(rozetka_price)
    driver.get(citrus)
    time.sleep(1)
    driver.implicitly_wait(5)
    citrus_price = driver.find_element_by_xpath("//div[@class='price']").text.split("грн")[0]
    print(citrus_price)
    driver.get(allo)
    driver.implicitly_wait(5)
    allo_price = driver.find_element_by_xpath("//span[@class='price']").text
    print(allo_price)
    driver.get(stylus)
    driver.implicitly_wait(5)
    stylus_price = driver.find_element_by_class_name("regular-price").text.split("грн")[0]
    print(stylus_price)

    print(id, cpu, speed, videocard, ram_type, ram, hd_type, hd, itbox_price, rozetka_price, citrus_price, allo_price,
          stylus_price)
    print(id.split("'")[1], cpu, speed, videocard, ram_type, ram, hd_type, hd, itbox_price.replace(' ', ''), rozetka_price.replace(' ', ''),
           citrus_price.replace(' ', ''), allo_price.replace(' ', ''), stylus_price.replace(' ', ''))
    sql = "INSERT INTO PC (id, cpu, speed, videocard, ram_type, ram, hd_type, hd, price_itbox, price_rozetka, " \
          "price_citrus, price_allo, price_stylus) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id.split("'")[1], cpu, speed, videocard, ram_type, ram, hd_type, hd, itbox_price.replace(' ', ''), rozetka_price.replace(' ', ''),
           citrus_price.replace(' ', ''), allo_price.replace(' ', ''), stylus_price.replace(' ', ''))
    cursor.execute(sql, val)
    mydb.commit()




def laptop(id):
    id = "'" + str(id) + "'"
    query = "select link_itbox, link_rozetka, link_citrus, link_allo, link_stylus  from contributors where id = " + id + ";"
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
    print(elements1)
    i = 0
    for elem in elements1:
        i = i + 1
        if elem == "Процессор":
            proc = elements1[i]
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
    cpu = proc.split("(")[0]
    speed = proc.split("(")[1].replace(')', '').split("GHz")[0]
    print(cpu, speed, videocard, ram_type, ram, hd_type, hd)
    itbox_price = driver.find_element_by_class_name("stuff-price").text.split("грн")[0]
    print(itbox_price)
    driver.get(rozetka)
    driver.implicitly_wait(10)
    rozetka_price = driver.find_element_by_class_name("product-prices__big").text.split("₴")[0]
    print(rozetka_price)
    driver.get(citrus)
    time.sleep(1)
    driver.implicitly_wait(10)
    citrus_price = driver.find_element_by_xpath("//div[@class='price']").text.split("грн")[0]
    print(citrus_price)
    driver.get(allo)
    driver.implicitly_wait(10)
    allo_price = driver.find_element_by_xpath("//span[@class='price']").text
    print(allo_price)
    driver.get(stylus)
    driver.implicitly_wait(10)
    stylus_price = driver.find_element_by_class_name("regular-price").text.split("грн")[0]
    print(stylus_price)

    print(id, cpu, speed, videocard, ram_type, ram, hd_type, hd, itbox_price, rozetka_price, citrus_price, allo_price,
          stylus_price)
    sql = "INSERT INTO laptop (id, cpu, speed, videocard, ram_type, ram, hd_type, hd, price_itbox, price_rozetka, " \
          "price_citrus, price_allo, price_stylus) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id.split("'")[1], cpu, speed, videocard, ram_type, ram, hd_type, hd, itbox_price.replace(' ', ''),
           rozetka_price.replace(' ', ''),
           citrus_price.replace(' ', ''), allo_price.replace(' ', ''), stylus_price.replace(' ', ''))
    cursor.execute(sql, val)
    mydb.commit()



def smartphone(id):
    id = "'" + str(id) + "'"
    query = "select link_itbox, link_rozetka, link_citrus, link_allo, link_stylus  from contributors where id = " + id + ";"
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
    print(elements1)
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
        if elem == "Фронтальная камера":
            front_cam = elements1[i]
        if elem == "Операционная система":
            os = elements1[i]
        if elem == "Цвет":
            color = elements1[i]
    print(cpu, diagonal, back_cam, front_cam, ram, color, os)
    itbox_price = driver.find_element_by_class_name("stuff-price").text.split("грн")[0]
    print(itbox_price)
    driver.get(rozetka)
    driver.implicitly_wait(5)
    rozetka_price = driver.find_element_by_class_name("product-prices__big").text.split("₴")[0]
    print(rozetka_price)
    driver.get(citrus)
    time.sleep(1)
    driver.implicitly_wait(5)
    citrus_price = driver.find_element_by_xpath("//div[@class='price']").text.split("грн")[0]
    print(citrus_price)
    driver.get(allo)
    driver.implicitly_wait(5)
    allo_price = driver.find_element_by_xpath("//span[@class='price']").text
    print(allo_price)
    driver.get(stylus)
    driver.implicitly_wait(5)
    stylus_price = driver.find_element_by_class_name("regular-price").text.split("грн")[0]
    print(stylus_price)

    print(id, cpu, diagonal, back_cam, front_cam, ram, color, os, itbox_price, rozetka_price, citrus_price, allo_price,
          stylus_price)
    sql = "INSERT INTO phone (id, cpu, diagonal, back_cam, front_cam, ram, color, os, price_itbox, price_rozetka, " \
          "price_citrus, price_allo, price_stylus) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id.split("'")[1], cpu, diagonal, back_cam, front_cam, ram, color, os, itbox_price.replace(' ', ''),
           rozetka_price.replace(' ', ''),
           citrus_price.replace(' ', ''), allo_price.replace(' ', ''), stylus_price.replace(' ', ''))
    cursor.execute(sql, val)
    mydb.commit()


if __name__ == '__main__':
    try:
        cycle(1)
    except:
        pass
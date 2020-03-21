# number = 0
# for number in range(10):
# number = number + 1
# if number == 5:
# continue    # вот оператор continue
# print('Number is ' + str(number))
# print('Out of loop')
#
# link = "('https://www.itbox.ua/product/Noutbuk_Apple_MacBook_Air_A1466_MQD32UA_A-p287994/',)"
# print(link)
# lin = link.split("'")
# print(lin)
# i = "1"
# query = "select link_itbox, link_rozetka, link_citrus, link_allo, link_stylus  from contributors where id = "+i+";"
# print(query)

# sql = "INSERT INTO PC (id, cpu, speed, videocard, ram_type, ram, hd_type, hd, price_itbox, price_rozetka, " \
#           "price_citrus, price_allo, price_stylus) " \
#           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# val = (2, 'Intel Core i5', 3.0, 'UHD Graphics 630', 'DDR4', 8, 'SSD', 256,  13999,  21499, 21499,  24999, 25830)
# print(sql, val)
# print("asf")
# a = "21 499";
# print(a.replace(' ', ''))
# id = 2
# id = "'"+str(id)+"'"
# print(id)
# sdg = "AMD Ryzen 5 3550H (2.1 - 3.7 GHz)"
# speed = sdg.split("(")[1].replace(')', '').split("GHz")[0]
# cpu = sdg.split("(")[0]
# print(speed)
# print(cpu)

# elements1 = ['Из отделения службы в среду 25.03, после 18:00\nВідділення №1: вул. Якова Шепеля, 1', 'Бесплатно', 'Курьером на адрес в четверг 26.03', 'Бесплатно', 'Серия (модельный ряд)', 'Apple MacBook Air', 'Тип ноутбука', 'Apple', 'Диагональ дисплея', '13.3"', 'Разрешение', 'WXGA+ (1440 х 900)', 'Поверхность экрана', 'глянцевая', 'Тип оперативной памяти', 'DDR3', 'Процессор', 'Intel Core i5 (1.8 ГГц)', 'Объем оперативной памяти', '8 ГБ', 'Объем SSD', '128 ГБ', 'Оптический привод', 'No ODD', 'Кардридер', 'Card-reader', 'Видеокарта', 'Intel HD Graphics', 'Веб-камера', 'FaceTime 720p HD', 'Дополнительные возможности', 'встроенный микрофон, стереодинамики', 'Беспроводные технологии', 'Wi-Fi, Bluetooth', 'Интерфейсы и подключения', 'Thunderbolt, 2 x USB 3.0, Комбинированный аудиоразъем', 'Операционная система', 'Mac OS Sierra', 'Заявленное время работы (часов)', '12', 'Особенности', 'алюминиевый корпус, подсветка клавиатуры', 'Вес', '1.35 кг', 'Цвет корпуса', 'Silver', 'Примечание', 'Производитель может менять свойства, характеристики, внешний вид и комплектацию товаров без предварительного уведомления']
# i = 0
# for elem in elements1:
#     i = i + 1
#     if elem == "Процессор":
#         proc = elements1[i]
#     if elem == "Модель видеокарты" or elem == "Видеокарта":
#         videocard = elements1[i]
#     if elem == "Тип оперативной памяти":
#         ram_type = elements1[i]
#     if elem == "Объем оперативной памяти":
#         ram = elements1[i].split("ГБ")[0]
#     if elem == "Типы внутренних накопителей"or elem == "Оптический привод":
#         hd_type = elements1[i]
#     if elem == "Объем HDD" or elem == "Объем SSD":
#         hd = elements1[i].split("ГБ")[0]
# cpu = proc.split("(")[0]
# speed = proc.split("(")[1].replace(')', '').split("GHz")[0]
# print(cpu, speed, videocard, ram_type, ram, hd_type, hd)
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="eShop"
)
cursor = mydb.cursor()

query = "select count(id) from contributors;"
cursor.execute(query)
counter = cursor.fetchone()
print(counter[0])

# sql = "INSERT INTO laptop (id, cpu, speed, videocard, ram_type, ram, hd_type, hd, price_itbox, price_rozetka, " \
#       "price_citrus, price_allo, price_stylus) " \
#       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# val = ('2', 'Intel Core i5',  '1.8 ГГц', 'Intel HD Graphics', 'DDR3', '8',  'No ODD', '128', '26273',
#        '24999', '24999',  '24999', '24999')
# cursor.execute(sql, val)
# mydb.commit()

id = 1
while id <= counter[0]:
    print("dsg")
    id = id + 1














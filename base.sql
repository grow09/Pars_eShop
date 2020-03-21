drop database if exists eShop;

create database eShop default charset utf8;

use eShop;

create table contributors (
id int auto_increment not null,
maker varchar(30) not null,
model varchar(30) not null,
type varchar(30) not null,
-- icon_itbox varchar(100),
-- icon_rozetka varchar(100),
-- icon_citrus varchar(100),
-- icon_allo varchar(100),
-- icon_stylus varchar(100),
link_itbox varchar(256),
link_rozetka varchar(256),
link_citrus varchar(256),
link_allo varchar(256),
link_stylus varchar(256),
img1 varchar(256),
img2 varchar(256),
img3 varchar(256),
primary key(id)
);

create table PC (
id int not null,
cpu varchar(30),
speed double,
videocard varchar(30),
ram_type varchar(10),
ram int,
hd_type varchar(4),
hd int,
price_itbox int,
price_rozetka int,
price_citrus int,
price_allo int,
price_stylus int,
foreign key (id) references contributors(id)
on delete cascade on update cascade
);

create table laptop (
id int not null,
cpu varchar(30),
speed varchar(30),
videocard varchar(30),
ram_type varchar(10),
ram int,
hd_type varchar(4) ,
hd int,
price_itbox double,
price_rozetka double,
price_citrus double,
price_allo double,
price_stylus double,
foreign key (id) references contributors(id)
on delete cascade on update cascade
);


create table phone (
id int not null,
diagonal double,
cpu varchar(30),
back_cam varchar(20),
front_cam varchar(20),
ram int not null,
color varchar(15),
os varchar(30),
price_itbox double,
price_rozetka double,
price_citrus double,
price_allo double,
price_stylus double,
foreign key (id) references contributors(id)
on delete cascade on update cascade
);

INSERT INTO `eShop`.`contributors` (`id`, `maker`, `model`, `type`, `link_itbox`, `link_rozetka`, `link_citrus`, `link_allo`, `link_stylus`, `img1`, `img2`, `img3`) VALUES (1, 'Lenovo', 'IdeaCentre A340-22IGM', 'PC', 'https://www.itbox.ua/product/Kompyuter_Lenovo_IdeaCentre_A340-22IGM_F0EA002DUA-p522191/', 'https://hard.rozetka.com.ua/lenovo_f0ea002gua/p104159094/', 'https://www.citrus.ua/noutbuki-i-ultrabuki/acer-swift-1-sf114-32-nxh1yeu014-obsidian-black-648948.html', 'https://allo.ua/ru/products/monobloki/artline-home-m34-m34v06.html', 'https://stylus.ua/asus-vivo-aio-v222ua-v222uak-ba159d-ua-p563961c384.html', 'https://img6.itbox.ua/1024x1024/prod_img/6/U0364856_big.jpg', 'https://img6.itbox.ua/1024x1024/prod_img/6/U0364856_2big.jpg', 'https://img6.itbox.ua/1024x1024/prod_img/6/U0364856_4big.jpg');
INSERT INTO `eShop`.`contributors` (`id`, `maker`, `model`, `type`, `link_itbox`, `link_rozetka`, `link_citrus`, `link_allo`, `link_stylus`, `img1`, `img2`, `img3`) VALUES (2, 'Apple', 'MacBook Air A1466', 'laptop', 'https://www.itbox.ua/product/Noutbuk_Apple_MacBook_Air_A1466_MQD32UA_A-p287994/', 'https://rozetka.com.ua/apple_mqd32ua_a/p17929266/?gclid=Cj0KCQjw09HzBRDrARIsAG60GP8ZGqmELpwITHfXGHvEATfk6Cjiw5bIbrIQ6dJ5bFCKSu-uE_wXgKAaAtOwEALw_wcB', 'https://www.citrus.ua/noutbuki-i-ultrabuki/apple-macbook-air-mqd32-614780.html', 'https://allo.ua/ru/products/notebooks/apple-a1466-macbook-air-mqd32ua-a.html', 'https://allo.ua/ru/products/notebooks/apple-a1466-macbook-air-mqd32ua-a.html', 'https://img7.itbox.ua/1024x1024/prod_img/7/U0247407_big.jpg', 'https://img7.itbox.ua/1024x1024/prod_img/7/U0247407_2big.jpg', 'https://img7.itbox.ua/1024x1024/prod_img/7/U0247407_4big.jpg');
INSERT INTO `eShop`.`contributors` (`id`, `maker`, `model`, `type`, `link_itbox`, `link_rozetka`, `link_citrus`, `link_allo`, `link_stylus`, `img1`, `img2`, `img3`) VALUES (3, 'Honor', '9X 4/128GB Midnight Black', 'phone', 'https://www.itbox.ua/product/Mobilniy_telefon_Honor_9X_4_128GB_Midnight_Black-p550256/', 'https://rozetka.com.ua/honor_9x_4_128gb_midnight_black/p106185207/?gclid=Cj0KCQjw09HzBRDrARIsAG60GP9vDraIXq7Y--WySrYoiwA_YBsPmHuFYaCotsAR6nEdc5zoJwWIOiIaAimeEALw_wcB', 'https://www.citrus.ua/smartfony/honor-9x-sapphire-blue-655738.html?gclid=Cj0KCQjw09HzBRDrARIsAG60GP83sstcPBGr0Tkw_ZNIE7_Wcd8G2xNmRA0993eIM3bxqAfIdvpgMLIaAuilEALw_wcB', 'https://allo.ua/ru/products/mobile/honor-9x-4-128gb-sapphire-blue_2.html', 'https://stylus.ua/honor-9x-4128gb-midnight-black-ua-ucrf-p564149c11256.html', 'https://img5.itbox.ua/1024x1024/prod_img/5/U0390115_big.jpg', 'https://img5.itbox.ua/1024x1024/prod_img/5/U0390115_2big.jpg', NULL);

select * from phone
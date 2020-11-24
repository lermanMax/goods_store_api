# goods_store_api


## Шаги для запуска сервиса

1. установить зависимости: pip install -r requirements.txt

2. запустить: python3 goods_store_api.py

## Тестовый сценарий

### Создать товар

curl -H "Content-Type: application/json" -X POST -d '{"new_product": {"name": "MyPhone", "discription": "Hello MyPhone", "options": [["color", "black"], ["diagonal", 6.5]]}}' http://127.0.0.1:5000/product
  
В ответ вы получите идентефикатор нового товара

### Получить товары по параметру

curl -H "Content-Type: application/json" --request GET -d '{"filter_option": "color", "filter_value": "black" }' http://127.0.0.1:5000/get_list

В ответ вы получите список всех товаров с параметром "color":"black"


### Получить детали товара

Вместо YOUR_PRODUCT_ID вставьте идентефикатор товара.   

curl -H "Content-Type: application/json" --request GET -d '{"product_id": "YOUR_PRODUCT_ID"}' http://127.0.0.1:5000/product

В ответ получите подробности запрошеного товара 

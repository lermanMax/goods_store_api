# goods_store_api


## Запуск сервиса

#### 1. Установить зависимостей: 
```
pip install -r requirements.txt
```
#### 2. Запустить: 
```
python3 goods_store_api.py
```
## Тестовый сценарий

#### 1. Создать товар
```
curl -H "Content-Type: application/json" -X POST -d '{"new_product": {"name": "MyPhone", "discription": "Hello MyPhone", "options": [["color", "black"], ["diagonal", 6.5]]}}' http://127.0.0.1:5000/product
```  
В ответ вы получите идентефикатор нового товара

#### 2. Получить товары по параметру
```
curl -H "Content-Type: application/json" --request GET -d '{"filter_option": "color", "filter_value": "black" }' http://127.0.0.1:5000/get_list
```
В ответ вы получите список всех товаров с параметром "color": "black"


#### 3. Получить детали товара

Вместо YOUR_PRODUCT_ID вставьте идентефикатор товара.   
```
curl -H "Content-Type: application/json" --request GET -d '{"product_id": "YOUR_PRODUCT_ID"}' http://127.0.0.1:5000/product
```
В ответ получите подробности запрошеного товара 

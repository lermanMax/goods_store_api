"""
REST API методы:
    
1. Создать новый товар (post_product)
2. Получить детали товара по ID (get_product)

3. Получить список названий товаров, с возможностью фильтрации по: (get_list)
    a) названию
    b) выбранному параметру и его значению

Методы принимают JSON на входе и отдают JSON на выходе.
"""
import json
import requests


url = "http://127.0.0.1:5000/"

class goods_test:

    def __init__(self, url_base):
        self.url_base = url_base
    
    def result_test(self, response, expected_code):
        
        result = '❌'
        if response.status_code == expected_code: result = '✅'
        
        try:
            return result, response.status_code, response.json()
        except:
            return result, response.content
        
    
    def get_product(self, expected_code, product_id):
        method = 'product'
        params = {"product_id": product_id}
        response = requests.get(self.url_base + method, params=params)
        
        return self.result_test(response, expected_code)
        
    
    def post_product(self, expected_code, product):
        method = 'product'
        json_ = {"new_product": product} 
        response = requests.post(self.url_base + method, json=json_)
        
        return self.result_test(response, expected_code)

    def get_list(self, expected_code, option, value):
        method = 'get_list'
        params = {'filter_option': option, 'filter_value': value }
        response = requests.get(self.url_base + method, params=params)
        
        return self.result_test(response, expected_code)
        



test = goods_test(url)

product = {"name": "XMIphone", 
           "discription": "Norm", 
           "options": [("color","black"),("diagonal", 6.5),("processor","GGXXXL")]
            } 

print('________________________________________')
print('START get_product tests')
print('test01 : ', test.get_product(200, '5fbd13e24ad81c943cb49423'))
print('test02 : ', test.get_product(400, ''))
print('test03 : ', test.get_product(404, '555555555555555555555555'))


print('________________________________________')
print('START post_product tests')
print('test01 : ', test.post_product(201, json.dumps(product)))
print('test02 : ', test.post_product(409, json.dumps(product)))
print('test03 : ', test.post_product(400, ''))


print('________________________________________')
print('START get_list tests')
print('test01 : ', test.get_list(200, 'name', None))
print('test02 : ', test.get_list(400, '',''))
print('test03 : ', test.get_list(404, 'not_option', 'blah'))
print('test01 : ', test.get_list(200, 'color', 'black'))




'''
#headers = {
#    'cache-control': "no-cache",
#}
#cookies = {
#    'ASP.NET_SessionId': 'dbyn3xdli5iugqtn1oulkyik',
#    'BPOFLogin': '047FD1144C4400DD103E52BF4D13E31F42E6BFA1A94D78C7E53071B116418CBADC61597EE5F7369A21E22C1E33540691EC546FA950916342E530AE56BA80CEF0DB988ABC681C66A79F0A98EAF5009569EE0CC6FAD7E14E537652AE2E1BCD50C3DFDF9013DC7D6AA8E7F0358FA97526E9',
#}
#data = {
#    'some_input_name': 'some input value',
#    'another_input_name': 'another input value',
#}
#files = {
#    'some_file_name': open('file.jpg', 'rb')
#}
#
#r = requests.post(url, headers=headers, cookies=cookies, data=data, files=files)
'''

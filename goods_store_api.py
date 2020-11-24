import json
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)
api = Api(app)

client = MongoClient('localhost', 27017)
db = client['goods_db']


def get_product(product_id):
    result = db.inventory.find_one({'_id': ObjectId(product_id)})
    
    if result: del result['_id'] #убираем из ответа поле ID, чтобы вернуть только детали товара 
    return result


def create_new_product(new_product):
    result = db.inventory.insert_one(new_product)
    return str(result.inserted_id)

def get_list(option):
    goods_list = []
    
    if option['filter_option'] == 'name':
        for item in db.inventory.find({}):
            goods_list.append(item['name'])
        goods_list.sort()
    
    else: 
        for item in db.inventory.find({}):
            for couple in item['options']: # проверка каждого параметра и его значения
                if couple[0] == option['filter_option']:
                    if couple[1] == option['filter_value']:
                        goods_list.append(item['name'])
            
         
    return goods_list



def abort_if_bad_product(new_product):
    # только проверка на пустую строку
    # можно доваить проверки на наличие всех ключей, не пустые значения и т.п. 
    if not new_product: 
        abort(400, message="Bad request")
    

def abort_if_product_exist(new_product):
    result = db.inventory.find_one(new_product)
    if result: 
        abort(409, message="Product already exist. It is available by this ID: {}".format(str(result['_id'])))
        
def abort_if_bad_id(product_id):
    if not product_id:
        abort(400, message="Bad request")  
        
def abort_if_product_doesnt_exist(result):
    if not result:
        abort(404, message="Product doesn't exist")
        
def abort_if_bad_option(option):
    if not option['filter_option']:
        abort(400, message="Bad request")  

def abort_if_list_doesnt_exist(result):
    if not result:
        abort(404, message="Option doesn't exist")



parser = reqparse.RequestParser()
parser.add_argument('product_id')
parser.add_argument('new_product')
parser.add_argument('filter_option')
parser.add_argument('filter_value')



class Product(Resource):    
    def get(self):
        args = parser.parse_args()
        product_id = args['product_id']
        abort_if_bad_id(product_id)
        
        result = get_product(product_id)
        abort_if_product_doesnt_exist(result)
        return result, 200

    def post(self):
        args = parser.parse_args()
        print(type(args['new_product']))
        abort_if_bad_product(args['new_product'])
        
        new_product = json.loads(args['new_product'])
        abort_if_product_exist(new_product)
        product_id = create_new_product(new_product)
        return {'product_id': product_id}, 201

class Get_list(Resource):
    def get(self):
        args = parser.parse_args()
        option = {}
        option['filter_option'] = args['filter_option']
        option['filter_value'] = args['filter_value']
        abort_if_bad_option(option)
        
        result = get_list(option)
        abort_if_list_doesnt_exist(result)
        
        return result, 200

    
api.add_resource(Product, '/product')
api.add_resource(Get_list, '/get_list')


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask,jsonify,request

app = Flask(__name__)

stores = [
    {
        'name': 'beautiful store',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
        ]
    },
    {
        'name': 'beautiful store 2',
        'items': [
            {
                'name': 'books',
                'price': 100
            }
        ]
    }
]

@app.route('/')
def home():
    return "it's home bro."

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if (store['name']==name):
            return jsonify(store['name'])   
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/item')
def get_item(name):
    for store in stores:
        if (store['name']==name):
            return jsonify(store['items'])  
    return jsonify({'message':'item not found'})

@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)    
    return jsonify(new_store)
        
@app.route('/store/<string:name>/item',methods=['POST'])
def add_item(name):
    req_data=request.get_json()
    for store in stores:
        if (store['name']==name):
            new_item={
                'name':req_data['name'],
                'price':req_data['price']
            }
            store['items'].append(new_item)    
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import pymongo

app = Flask(__name__)

try:
    client = pymongo.MongoClient(f"mongodb+srv://SachinGuldagad:Sachin123@cluster0.zpxoi.mongodb.net/MyFirstDatabase?retryWrites=true&w=majority")
    database_name=client['Testing']
    flag=0
    if database_name['FirstCollection'].find_one({"Emp_id":request.form['emp_id']}):
        flag=1
except:
    print("CANNOT connect to db")

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():

    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        if flag==0:
            employee={"Emp_id":request.form['emp_id'], "username": request.form['username'],"Fname":request.form['Fname'],
                "Lname":request.form['Lname'], "Password": request.form['Password']}
            collection_name=database_name['FirstCollection']
            collection_name.insert_one(employee)
            return '''<h1>Result is {}:</h1>'''.format('Create User Succeed')
        else:
            return '''<h1>Result is {}:</h1>'''.format('Create User Failed')
    except:
        return '''<h1>Result is {}:</h1>'''.format('Create User Failed')

@app.route('/update_user', methods=['POST'])
def update_user():
    try:
        #if flag==1:
        database_name.FirstCollection.find_one_and_update({"Emp_id":request.form['emp_id']},{'$set': { 'Lname': request.form['Lname']}})
        return '''<h1>Result is {}:</h1>'''.format('User Updated Successfully')
        #else:
        #    return '''<h1>Result is {}:</h1>'''.format('Update User Failed')
    except:
        return '''<h1>Result is {}:</h1>'''.format('Update User Failed')

@app.route('/get_user', methods=['POST'])
def get_user():
    user_details=database_name['FirstCollection'].find_one({"Emp_id":request.form['emp_id']})
    return '''<h1>My result is in update{}:</h1>'''.format(user_details)

@app.route('/login', methods=['POST'])
def user_login():
    if (request.method=='POST'):
        flag1=0
        if database_name['FirstCollection'].find_one({"username":request.form['username']}) and database_name['FirstCollection'].find_one({"Password":request.form['password']}):
            flag1=1
        if flag1==1:
            return '''<h1>My result is in update{}:</h1>'''.format("Login is successful")
        else:
            return '''<h1>My result is in update{}:</h1>'''.format("Login is unsuccessful")


@app.route('/sachin')
def url_test():
    num1=request.args.get('val1')
    num2=request.args.get('val2')
    num3=num1+num2
    return '''<h1>My result is {}:</h1>'''.format(num3)

collection_name=''
@app.route('/mongodb', methods=['POST'])
def mongodb_database():
    username=request.json['username']
    password=request.json['password']
    db_name=request.json['database']


    cltn_name=request.json['collection_name']

    return database_name, collection_name

@app.route('/mongodb/insert_documents', methods=['POST'])
def mongodb_collections():
    print("Inside Create mongodb_collections method")
    #collection_name = dbname["user_1_items"]
    self.mongodb_database()
    username=request.json['username']
    password=request.json['password']
    db_name=request.json['database']
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.zpxoi.mongodb.net/{db_name}?retryWrites=true&w=majority")
    database_name=client[f'{db_name}']
    cltn_name=request.json['collection_name']
    collection_name=database_name[f'{cltn_name}']

    item_1 = {
    "_id" : "112",
    "item_name" : "rsfsws",
    "max_discount" : "13%",
    "batch_number" : "0FRsfsfG",
    "price" : 340,
    "category" : "applsfsfiance"
    }

    item_2 = {
    "_id" : "0213",
    "item_name" : "gdf",
    "category" : "osdfsd",
    "quantity" : 2,
    "price" : 3,
    "item_description" : "eggsdfss"
    }
    collection_name.insert_many([item_1,item_2])
    return '''<h1>My result is {}:</h1>'''.format(database_name.list_collection_names())

@app.route('/mongodb/find', methods=['POST'])
def monogodb_find():
    print("inside update function")
    username=request.json['username']
    password=request.json['password']
    db_name=request.json['database']
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.zpxoi.mongodb.net/{db_name}?retryWrites=true&w=majority")
    database_name=client[f'{db_name}']
    cltn_name=request.json['collection_name']
    collection_name=database_name[f'{cltn_name}']
    item_details = collection_name.find_one({"_id":"02"})
    return '''<h1>My result is in update{}:</h1>'''.format(item_details)

@app.route('/mongodb/delete', methods=['POST'])
def monogodb_delete():
    print("inside update function")
    username=request.json['username']
    password=request.json['password']
    db_name=request.json['database']
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.zpxoi.mongodb.net/{db_name}?retryWrites=true&w=majority")
    database_name=client[f'{db_name}']
    cltn_name=request.json['collection_name']
    collection_name=database_name[f'{cltn_name}']
    delete= collection_name.delete_one({"_id":"02"})
    return '''<h1>My result is {}:</h1>'''.format(delete)

if __name__ == '__main__':
    app.run()
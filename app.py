from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import json
from dotenv import load_dotenv 
import os
load_dotenv()
app = Flask(__name__)

    
mongo_username = os.environ.get("MONGO_USERNAME")
mongo_password = os.environ.get("MONGO_PASSWORD")
mongo_host = os.environ.get("MONGO_HOST")
mongo_db = os.environ.get("MONGO_DB")

client = MongoClient(f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_host}/")
db = client.get_database(mongo_db)

vendor_collection_name = "Vendor"
user_collection_name = "User"

vendor_collection = db.get_collection(vendor_collection_name)
user_collection = db.get_collection(user_collection_name)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vendor-registration', methods = ["GET", "POST"])
def vendor_registration():
    if request.method=="POST":
        name=request.form.get('name')
        email= request.form.get('email')
        address = request.form.get('first_address')
        mobile= request.form.get('tel')
        companyNo = request.form.get('companyNo')
        product = request.form.get('product')
        print(name)
        print(email)
        print(address)
        print(mobile)
        print(companyNo)
        print(product)
        vendor_data = {
            "name": name,
            "email": email,
            "address": address,
            "mobile": mobile,
            "companyNo": companyNo,
            "productDetail": product
        }
        vendor_collection.insert_one(vendor_data)
        return redirect("/")
    return render_template('form.html')

@app.route('/user-registration',methods = ["GET", "POST"])
def user_registration():
    if request.method=="POST":
        name=request.form.get('name')
        email= request.form.get('email')
        mobile= request.form.get('tel')

        vendor_data = {
            "name": name,
            "email": email,
            "mobile": mobile
        }
        user_collection.insert_one(vendor_data)
        return redirect("/")
    return render_template('form2.html')

@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route('/event')
def event():
    return render_template("event.html")
if __name__ == '__main__':
    app.run(debug=True, host ="0.0.0.0")

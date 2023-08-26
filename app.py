from flask import Flask, render_template, request
from pymongo import MongoClient
import base64

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://password:password@cluster0.btuijp0.mongodb.net/?retryWrites=true&w=majority")
db = client["identity_cards"]
collection = db["cards"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
@app.route("/submit", methods=["POST"])
def submit():
    full_name = request.form.get("full_name")
    age = int(request.form.get("age"))
    address = request.form.get("address")
    image = request.files["image"]

    try:
        # Read and encode the image data
        image_data = image.read()
        encoded_image = base64.b64encode(image_data).decode("utf-8")

        # Insert data into MongoDB
        card_data = {
            "full_name": full_name,
            "age": age,
            "address": address,
            "image": encoded_image
        }
        collection.insert_one(card_data)

        return "Identity card submitted successfully!"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)

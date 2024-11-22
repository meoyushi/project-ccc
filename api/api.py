from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Cafe Delight API"

@app.route('/menu')
def get_menu():
    menu = {
        "items": [
            {"name": "Coffee", "price": "$3.00"},
            {"name": "Pastries", "price": "$2.50"},
            {"name": "Breakfast Specials", "price": "$6.00"}
        ]
    }
    return jsonify(menu)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, static_folder='static')
connection = sqlite3.connect("database.sqlite")
cursor = sqlite3.Cursor(connection)



def make_product_card(info, cards=None):
    products = cursor.execute("SELECT * FROM products").fetchall()
    name = str(info[1])
    description = str(info[2])
    price = str(info[3]) + " UAH"
    print(name, description, price)
    for product in products:
        cards.append(make_product_card(product))
    return f'<div class="product-card"><h3>{name}</h3><p>{description}</p><p>{price}</p></div>'


@app.route('/')
def index():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT * FROM products").fetchall()
    connection.close()
    print(cards)
    return render_template('index.html', cars=cards)


@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/index2")
def index2():
    return render_template('index2.html')


@app.route("/purchase/<car>")
def purchase(car):
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    car1 = cursor.execute(f"SELECT * FROM products WHERE name LIKE '%{car}%'").fetchone()
    connection.close()
    print(car)
    return render_template('car_page.html', car=car1)

@app.route("/page9")
def page9():
    return render_template('page9.html')

@app.route("/products")
def products():
    return render_template('products.html')

@app.route("/Privacy")
def Privacy():
        return render_template('Privacy.html')

@app.route("/page3")
def page3():
        return render_template('page3.html')

@app.route("/Return")
def Return():
        return render_template('Return.html')



if __name__ == "__main__":
    app.run(debug=True)

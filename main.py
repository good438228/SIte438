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
    return render_template('index.html')


@app.route("/result")
def result():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT * FROM products").fetchall()
    connection.close()
    return render_template('products.html', products=cards)


@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/index2")
def index2():
    return render_template('index2.html')


@app.route("/page2")
def page2():
    return render_template('page2.html')


@app.route("/page3")
def page3():
    return render_template('page3.html')


@app.route("/page4")
def page4():
    return render_template('page4.html')


@app.route("/page5")
def page5():
    return render_template('page5.html')


@app.route("/page6")
def page6():
    return render_template('page6.html')


@app.route("/page7")
def page7():
    return render_template('page7.html')


@app.route("/page8")
def page8():
    return render_template('page8.html')

@app.route("/page9")
def page9():
    return render_template('page9.html')

@app.route("/products")
def products():
    return render_template('products.html')




    return render_template('products.html', products=cards)


if __name__ == "__main__":
    app.run(debug=True)

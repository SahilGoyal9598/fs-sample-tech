from flask import Flask, render_template, jsonify
from database import load_orders_from_db, load_order_from_db

app = Flask(__name__)


# decorator in python "@"
@app.route("/")  #home page
def hello_world():
  orders = load_orders_from_db()

  return render_template("home.html", orders=orders)


@app.route("/cancel/<id>")
def show_order(id):
  orders = load_order_from_db(id)
  if not orders:
    return "Not found", 404
  return render_template("single_order.html", orders=orders)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

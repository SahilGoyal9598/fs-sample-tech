from flask import Flask, render_template
from database import load_orders_from_db

app = Flask(__name__)




# decorator in python "@"
@app.route("/")  #home page
def hello_world():
  orders = load_orders_from_db()

  return render_template("home.html", orders=orders)


print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

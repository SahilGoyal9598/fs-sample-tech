from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_orders_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from order_details"))

    orders = []
    for row in result.all():
      orders.append(row._mapping)
  return orders


# decorator in python "@"
@app.route("/")  #home page
def hello_world():
  orders = load_orders_from_db()

  return render_template("home.html", orders=orders)


print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

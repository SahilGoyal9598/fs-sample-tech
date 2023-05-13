from flask import Flask, render_template, jsonify

app = Flask(__name__)

order_details = [{
  'id': 1,
  'unique_id': 123878548047,
  'order no': '#200268987',
  'sku': 'TP500BLUE-XXL',
  'status': 'in cutting'
}, {
  'id': 2,
  'unique_id': 123878548089,
  'sku': 'DR500BLUE-M',
  'status': 'in finishing'
}, {
  'id': 3,
  'unique_id': 123878548090,
  'order no': '#200268876',
  'sku': 'KNTR121-BLAC-XXL',
  'status': 'dispatched'
}, {
  'id': 4,
  'unique_id': 123878548056,
  'order no': '#200268845',
  'sku': 'KNTR152GREY-L',
  'status': 'Cancelled'
}]


# decorator in python "@"
@app.route("/")  #home page
def hello_world():
  return render_template("home.html", orders=order_details)


@app.route("/orders")  # orders page
def orders():
  return jsonify(order_details)


print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

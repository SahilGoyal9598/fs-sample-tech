from flask import Flask, render_template, jsonify, request
from database import load_orders_from_db, load_order_from_db, add_cancel_to_db, add_scan_unique_to_db, add_new_orders_to_db, order_tracking_filter, all_orders
import csv
from datetime import datetime
#import pandas as pd

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


@app.route("/cancel/<id>/apply", methods=['post'])
def apply_to_order(id):
  data = request.form
  add_cancel_to_db(id, data)

  return jsonify(data)
  # store to th Database
  # send an confirmation email
  # Display the acknoledgement


@app.route("/scan", methods=['GET'])
def scan_page():
  return render_template("scan_page.html")


@app.route("/scan_order", methods=['POST'])
def scan_order_in_production():
  scan_id = request.form['unique_id_scan']
  scan_status = request.form['scan_status']
  add_scan_unique_to_db(scan_id, scan_status)

  return render_template("scan_page.html")


@app.route("/new_orders", methods=['GET'])
def show_new_order_page():
  return render_template("fresh_orders.html")


@app.route("/upload", methods=['POST'])
def add_new_order():
  csvFile = request.files['csvFile']
  csv_data = csvFile.read().decode('utf-8').splitlines()
  csv_reader = csv.reader(csv_data)
  next(csv_reader)  # skip header row if needed

  for row in csv_reader:
    unique_id = row[0]
    order_no = row[1]
    order_status = row[2]
    orderDate = row[3]
    tmpDate = orderDate.split('-')
    dateString = tmpDate[0] + '/' + tmpDate[1] + '/' + tmpDate[2][2:4:1]
    order_date = datetime.strptime(dateString, '%d/%m/%y').date()
    # print('ola')
    # print(order_date)
    # print('ola')
    # order_date = datetime.strptime(order_date, "%d-%m-%y").strftime("%y-%m-%d")

    add_new_orders_to_db(unique_id, order_no, order_status, order_date)
  return render_template("fresh_orders.html")

  return "Invalid CSV file"


@app.route("/all_orders")
def show_all_orders():
  all_order = all_orders()
  return render_template("all_orders.html", all_order=all_order)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

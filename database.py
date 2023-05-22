from sqlalchemy import create_engine, text
import os

# this will connect to the database

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_orders_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from order_details"))

    orders = []
    for row in result.all():
      orders.append(row._mapping)
  return orders


def load_order_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from order_details where id = {id}"))
    rows = []
    for row in result.all():
      rows.append(row._mapping)

    if len(rows) == 0:
      return None
    else:
      return [dict(row) for row in rows]


def add_cancel_to_db(id, data):
  with engine.connect() as conn:

    query = text(
      f"insert into order_status_log (order_id, unique_id) values ('{id}','{data}')"
    )

    conn.execute(query)


def add_scan_unique_to_db(scan_id, scan_status):
  with engine.connect() as conn:

    query = text(
      f"insert into order_status_log (unique_id, order_status) values ('{scan_id}','{scan_status}')"
    )
    conn.execute(query)


def add_new_orders_to_db(scan_id, order, status, date):
  with engine.connect() as conn:

    query = text(
      f"insert into orders (unique_id,order_no,order_status,order_date) values ('{scan_id}','{order}','{status}','{date}')"
    )
    conn.execute(query)


def order_tracking_filter():
  with engine.connect() as conn:

    query = text(
      f"select distinct(order_status) from orders order by order_status ")

  order_status = []
  for row in query.all():
    order_status.append(row._mapping)
  return order_status


def all_orders():
  with engine.connect() as conn:
    query = text("select * from orders limit 10")
    result = conn.execute(query)

    all_orders_data = []
    for row in result.all():
      all_orders_data.append(row._mapping)
    return all_orders_data

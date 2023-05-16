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

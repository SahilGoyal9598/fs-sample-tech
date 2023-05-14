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

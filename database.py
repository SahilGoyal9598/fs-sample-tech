from sqlalchemy import create_engine

# this will connect to the database

db_connection_string = "mysql+pymysql://2g14et2l6l8wqx85z9xj:pscale_pw_DpVW0QX0rUsQzVQBb9uWFGZSQeoUiq6yfXBi8GCkMAZ@aws.connect.psdb.cloud/fs-sample-tech?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

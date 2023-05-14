from sqlalchemy import create_engine

# this will connect to the database

db_connection_string = "mysql+pymysql://07w6gigu86t6fo0rnime:pscale_pw_Bx5P7Bi34K8BTDjkMDOrfBxczgueZmzkXNEz9SiQ2tF@aws.connect.psdb.cloud/fs-sample-tech?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

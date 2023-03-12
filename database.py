from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://r02sjowi8fmff2uxmvqc:pscale_pw_xR8bcA9CMPUOnKesvFJAJJ83RcRWSWDn1wjUrLwtETV@ap-south.connect.psdb.cloud/careers_thadomal?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())

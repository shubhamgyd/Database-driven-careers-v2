import os
import sqlalchemy
from sqlalchemy import create_engine, text

# my_secret = os.environ['DB_CONNECTION_STRING']

print(sqlalchemy.__version__)
# my_secret = os.environ['DB_CONNECTION_KEY']

db_connection_string= os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))

#   '''
#   print("type(result):", type(result))
#   result_all = result.all()
#   print("type(result.all())", type(result_all))
#   first_result = result_all[0]
#   print("type(first_result):",type(first_result))

#   # Here we have converted alchemy row which is of type row to dictionary.
#   first_result_dict = dict(result_all[0])
#   print("type(first_result_dict):", type(first_result_dict))
#   print(first_result_dict)
#   '''
  
#   result_dicts = []

#   for row in result.all():
#     result_dicts.append(row._mapping)
#     print(result_dicts)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs
      
  
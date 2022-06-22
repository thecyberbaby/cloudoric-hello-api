import os
import mysql.connector
import json
from flask import Flask


app = Flask(__name__)

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')


@app.route('/')
def hello_cloudoric():
  return 'Hello, Cloudoric!\n'

@app.route('/healtz')
def healthy():
  return 'Healtz Endpoint says app is healthy.\n'

@app.route('/widgets')
def get_widgets() :
  mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_pass,
    database=db_name
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM widgets")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)


if __name__ == "__main__":
  app.run(host ='0.0.0.0')
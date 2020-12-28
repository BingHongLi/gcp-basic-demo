#
# curl http://169.254.169.254/computeMetadata/v1/instance/attributes/ -H "Metadata-Flavor: Google"

import requests

db_host_res=requests.get('http://169.254.169.254/computeMetadata/v1/instance/attributes/db_host', headers = {'Metadata-Flavor': 'Google'})
db_host=db_host_res.text

db_user_res=requests.get('http://169.254.169.254/computeMetadata/v1/instance/attributes/db_user', headers = {'Metadata-Flavor': 'Google'})
db_user=db_user_res.text

db_password_res=requests.get('http://169.254.169.254/computeMetadata/v1/instance/attributes/db_password', headers = {'Metadata-Flavor': 'Google'})
db_password=db_password_res.text

import pymysql

# 建立連線
connection = pymysql.connect(host=db_host,
                             user=db_user,
                             password=db_password)


# 查詢有多少databases
some_sql_sentences= connection.cursor()
print(some_sql_sentences.execute("SHOW DATABASES"))




import pymysql

# 透過cloud shell editor
# 先在terminal 使用 cloud_sql_proxy 與cloudSQL建立連線，將request導至本地的3306 Port
# cloud_sql_proxy -instances=gcp-practice-123:asia-east1:test-sql=tcp:3306

# 建立連線
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='cxcxc')


# 查詢有多少databases
some_sql_sentences= connection.cursor()
print(some_sql_sentences.execute("SHOW DATABASES"))


import mysql.connector

class SQLClass:
   
   #def __init__(self):

    def connect():
        config = {
            'user': 'root',
            'password': 'administrator',
            'host': 'localhost',
            'port': '3306',
            'database': 'BIABLE01',
            'raise_on_warnings': True
        }
   
        try:
            cnx = mysql.connector.connect(**config)
            return cnx
          
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
    

    def getQueryData(cnx, typeOfQuery, codeEntity):
        file = open("SQL/" + typeOfQuery + ".sql", "r", encoding='utf-8-sig')
        query = file.read()

        try:
            if codeEntity and query:
                query = query.replace("{0}", codeEntity);

            print("query executed: \n", query)
            cursor = cnx.cursor()
            cursor.execute(query)
            myresult = cursor.fetchall()

            return myresult

        except mysql.connector.cursor.errors.Error as err:
            print(err)
from Bussiness import SQLBussiness
from Bussiness import XMLBussiness
import datetime

def main():
    print("WELCOME TO ACINOX-PYTHON PROJECT \n\n")

    fecha = datetime.datetime.now().strftime("%Y%m%d.%H%M")
    
    conn = SQLBussiness.SQLClass.connect()
    sqlResult1 = SQLBussiness.SQLClass.getQueryData(conn, "sociedades", "")
    #sqlResult2 = SQLBussiness.SQLClass.getQueryData(conn, "contactos", "01")

    XMLBussiness.XMLClass.GenerateXML(sqlResult1, "sociedades", fecha)
    #XMLBussiness.XMLClass.GenerateXML(sqlResult2, "clientes", fecha)
   
    

if __name__ == '__main__':
    main()
from Bussiness import SQLBussiness
from Bussiness import XMLBussiness
from Bussiness import XSDBussiness
import datetime

def main():
    print("WELCOME TO ACINOX-PYTHON PROJECT \n\n")

    date = datetime.datetime.now().strftime("%Y%m%d.%H%M")
    
    conn = SQLBussiness.SQLClass.connect()
    sqlResult1 = SQLBussiness.SQLClass.getQueryData(conn, "sociedades", "")
    #sqlResult2 = SQLBussiness.SQLClass.getQueryData(conn, "contactos", "01")

    #XMLBussiness.XMLClass.GenerateXML(sqlResult1, "sociedades", date)
    #XMLBussiness.XMLClass.GenerateXML(sqlResult2, "clientes", fecha)
   
    XSDBussiness.XSDClass.ValidateXML("sociedades", date)
    

if __name__ == '__main__':
    main()
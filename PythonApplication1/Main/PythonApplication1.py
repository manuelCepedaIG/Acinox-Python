from Bussiness import SQLBussiness


def main():
    print("WELCOME TO ACINOX-PYTHON PROJECT \n\n")

    conn = SQLBussiness.SQLClass.connect()
    SQLBussiness.SQLClass.getQueryData(conn, "sociedades", codeEntity = None)
    
    print("\nDone. Press any key to close.")

if __name__ == '__main__':
    main()
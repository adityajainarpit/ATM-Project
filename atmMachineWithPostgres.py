import psycopg2

# def create_bank():
#     try:
#         conn=psycopg2.connect(database="sbibank",
#                               host="localhost",
#                               user="postgres",
#                               password="Adi123")
#         cursor=conn.cursor()
#         cursor.execute("CREATE TABLE sbiaccount(accountno bigint not null primary key,name varchar not null,amount integer not null)")
#         conn.commit()
#         print("Table created successfully")
#     except(Exception,psycopg2.error) as error:
#         print("Failed to create the table",error)
#     finally:
#         if conn:
#             cursor.close()
#             conn.close()
#             print("Connection closed successfully")
# def insert_Details():
#     try:
#         conn=psycopg2.connect(database="sbibank",
#                               host="localhost",
#                               user="postgres",
#                               password="Adi123")
#         cursor=conn.cursor()
#         insertQuery="""INSERT INTO sbiaccount VALUES(%s,%s,%s)"""
#         account=[]
#         accno=int(input("Please enter the account No. "))
#         account.append(accno)
#         name=input("Please enter the Name ")
#         account.append(name)
#         amt=int(input("Please enter the amount you want to add "))
#         account.append(amt)
#         tuple(account)
#         cursor.execute(insertQuery,account)
#         conn.commit()
#         print("Data Inserted Successfully ")
#     except(Exception,psycopg2.Error) as error:
#         print("Failed to insert the Data",error)
#     finally:
#         if conn:
#             cursor.close()
#             conn.close()
            # print("Connection closed successfully")
# create_bank()
# while True:
#     insert_Details()

def chk_user(accno):
    try:
        conn=psycopg2.connect(database="sbibank",
                              host="localhost",
                              user="postgres",
                              password="Adi123")
        cursor=conn.cursor()
        quer=f"""SELECT * FROM sbiaccount WHERE accountno={accno}"""
        # quer="""SELECT * FROM sbiaccount WHERE accountno='%d'"""
        # val=3618484956
        cursor.execute(quer)
        print(cursor.fetchone())
        data=cursor.fetchone()
        return data

        # conn.commit()
        
        # print("Table created successfully")
    except(Exception,psycopg2.Error) as error:
        print("Failed to create the table",error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            # print("Connection closed successfully")
def add_Account():
    try:
        conn=psycopg2.connect(database="sbibank",
                              host="localhost",
                              user="postgres",
                              password="Adi123")
        cursor=conn.cursor()
        insertQuery="""INSERT INTO sbiaccount VALUES(%s,%s,%s)"""
        account=[]
        accno=int(input("Please enter the account No. "))
        account.append(accno)
        name=input("Please enter the Name ")
        account.append(name)
        amt=int(input("Please enter the amount you want to add "))
        account.append(amt)
        tuple(account)
        cursor.execute(insertQuery,account)
        conn.commit()
        print("Data Inserted Successfully ")
    except(Exception,psycopg2.Error) as error:
        print("Failed to insert the Data",error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")
def update_amt(accno,amt):
    try:
        conn=psycopg2.connect(database="sbibank",
                              host="localhost",
                              user="postgres",
                              password="Adi123")
        cursor=conn.cursor()
        quer=f"""UPDATE sbiaccount SET amount={amt} WHERE accountno={accno}"""
        if cursor.execute(quer):
            conn.commit()
            return True
            # print("Data updated successfully")
        else:
            return False
    except(Exception,psycopg2.Error) as error:
        print("Failed to update the Data",error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")
# accno=int(input("Please enter the account no." ))
# amt=int(input("Please enter the amount you want to set "))
# res=update_amt(accno,amt)
# print(res)
def delete_acc(accno):
    try:
        conn=psycopg2.connect(database="sbibank",
                              host="localhost",
                              user="postgres",
                              password="Adi123")
        cursor=conn.cursor()
        quer=f"""DELETE FROM sbiaccount WHERE accountno={accno}"""
        cursor.execute(quer)
        conn.commit()
        print("Account deleted Successfully")
    except(Exception,psycopg2.Error) as error:
        print("Failed to delete the Data",error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed successfully")
# accno=    ssint(input("Please enter the account no." ))
# res=delete_acc(accno)
# print(res)

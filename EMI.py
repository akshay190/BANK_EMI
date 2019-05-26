import pymysql
import math
db=pymysql.connect("localhost","root","","data_science")
cursor=db.cursor()

print("Hi! Welcome in My EMI Loan Transation System ")
print("We Provide Following Services : ")
while(1):
    print("****************************************************************************")
    print(1," Create An Loan Table ")
    print(2," Create An EMI Table ")
    print(3," Add Account In Loan Table And EMI Table ")
    print(4," Show All The Loan Table Detail ")
    print(5," Show All The EMI Table Detail ")
    print(6," Show All The User Detail On Console ")
    print(7," Exit ")
    print("****************************************************************************")
    n=int(input("Enter Your Choice  :"))
    if(n==1):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "loan" in l:
            print("Table Already Exist in Database ")
        else:
            sql="create table loan(id int primary key,LoanAmount double);"
            cursor.execute(sql)
            print("DataBase Bank Table Schema Formed")
        input("Press Enter To Continue :")
    if(n==2):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "emi" in l:
            print("Table Already Exist in Database ")
        else:
            sql="create table emi(id int auto_increment primary key,emi_amount varchar(50),rate int,No_Month int,loan_id int);"
            cursor.execute(sql)
            print("DataBase Bank Table Schema Formed")
        input("Press Enter To Continue :")
    if(n==3):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if (("loan" in l) and("emi" in l)):
            id1=int(input("Please Enter Loan Id Number : "))
            balance=float(input("Please Enter Loan Amount  : "))
            rate=int(input("Enter Rate In Percantage : "))
            number=int(input("Enter Number Of Months : "))
            if(balance>=0):
                emi_amount=(balance+(balance*rate/100))/number
                sql="insert into loan values('%i','%d')"%(id1,balance)
                r=cursor.execute(sql);
                db.commit()
                sql="insert into emi(emi_amount,rate,No_Month,loan_id)values('%s','%i','%i','%i')"%(str(emi_amount),rate,number,id1)
                r=cursor.execute(sql);
                db.commit()
                print("Your EMI Amount Is ",emi_amount,"for ",number,"Months","And Total Aount Is ",emi_amount*number)
                print("Your Loan Account is Registered ")
            else:
                print("Please Enter Positive Balance Amount ")
        else:
            print("You Must Create Both Table Schema ")
        input("Press Any Key To Continue ")
        
    if(n==4):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "loan" in l:
            sql="select * from loan"
            cursor.execute(sql)
            x=cursor.fetchall()
            if(x):
                print("Loan User Detail : ")
                print("Loan Id    Loan Amount")

                for i in x:
                    for j in i:
                        print(j,end="\t\t")
                    print()
            else:
                print("You Have No Loan User Please Give Some Loan To User ")
        else:
            print("Please Database Schema Create")
        input("Press Enter To Continue :")
        
    if(n==5):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "emi" in l:
            sql="select * from emi"
            cursor.execute(sql)
            x=cursor.fetchall()
            if(x):
                print("Loan User EMI Detail : ")
                print("Id  EMIAmount    Rate  No.Of Months  Loan_id")

                for i in x:
                    print(i[0],end="\t")
                    print(math.ceil(float(i[1])),end="\t")
                    print(i[2],end="\t")
                    print(i[3],end="\t\t")
                    print(i[4])
            else:
                print("You Have No Loan User Please Give Some Loan To User ")
        else:
            print("Please Database Schema Create")
        input("Press Enter To Continue :")


            
    if(n==6):
        sql="show tables"
        cursor.execute(sql);
        x=cursor.fetchall()
        l=[]
        for i in x:
            l=l+[i[0]]
        if "emi" in l:
            sql="select * from emi"
            cursor.execute(sql)
            x=cursor.fetchall()
            if(x):
                print("User Detail : ")
                print("S.No.  Loan Amount   Rate   Number Of Months\t Total Amount \tEMI AMOUNT")
                for i in x:
                    sql="select * from loan where id = %i"%(i[4])
                    cursor.execute(sql)
                    x=cursor.fetchall()
                    print(i[0],end="\t")
                    print(x[0][1],end="\t\t")
                    print(str(i[2])+"%",end="\t")
                    print(i[3],end="\t\t")
                    print(float(i[1])*i[3],end="\t\t")
                    emi_amount=(float(i[1])*i[3])/i[3]
                    if(emi_amount==math.floor(emi_amount)):
                        print(emi_amount)
                    else:
                        print(emi_amount,"=",math.ceil(emi_amount))
            else:
                print("You Have No Loan User Please Give Some Loan To User")
        else:
            print("Please Database Schema Create")
        input("Press Enter To Continue :")
   

        
    if(n==7):
        break
    if(n<1 or n>7):
        print("You Enterd Wrong Number")
        print("Please Enter Right Choice")
        input("Press Enter To Continue : ")
    


print("Thank You For Using My EMI Loan System")
print("See You Again ")

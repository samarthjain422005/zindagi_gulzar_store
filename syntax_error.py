import mysql.connector
con = mysql.connector.connect(user='root', password='', host='localhost', database='project')
def add_data():
    1="select max(bill_number) from billing"
    cur=con.cursor()
    cur.execute(l)
    rec=cur.fetchall()
    B=rec[0][0]
    bill_no=B+1
    name=input("Enter the Name of the Customer: ")
    date=input("Enter the Date of Billing: ")
    mobile_no=int(input("Enter the Customer's Mobile Number: ")
    no_of_item=int(input("Enter the Number of Items Purchased: "))
    maxitem=9
    if (no_of_item>maxitem):
        print()
        print("Please enter less than 9 items or split the bill into two")
    elif (no_of_item≤maxitem) :
        for a in range(1, no_of_item+1):
            s_no=str(bill_no)+'xx'+str(a)
            product_code=input("Enter the Product Code: ")
            s="select * from products where product_id='{}'".format(product_code)
            cur=con.cursor()
            cur.execute(s)
            rec=cur.fetchall()
            for r in rec:
                product_name=r[2]
                mrp=r[3]
                sgst=r[4]
                cyst=r[5]
                qty=r[6]
                stock available=r[7]
            quantity=int(input("Enter Quantity: "))
            t=(mrp+sgst+cgst)*quantity
            i="insert into billing values({},'{}','{}','{}','{}','{}','{}',{},{},{},{},{})".format(bill_no, s_no, date, name, mobile_no, product_name, product_code, mrp, quantity, sgst, cgst, t)
            cur=con.cursor()
            cur.execute(i)
            con. commit()
            p="update products set stock={} where product_id='{}'".format(stock_available-quantity, product_code)
            cur=con.cursor()
            cur.execute(p)
            con.commit()
            w=qty+quantity
            q="update products set quantity_sold={} where product_id='{}'".format(w, product_code)
            cur=con.cursor)
            cur.execute(q)
            con. commit()
            d="select * from due_taxes where product_id='{}'".format(product_code)
            cur.execute(d)
            record=cur.fetchall()
            for u in record:
                quantity_sold=u[2]+quantity
                gst_collected=u[3]+(sgst+cgst)*quantity
                v="update due_taxes set quantity_sold={}, gst_collected={}, status='Due' where product_id='{}'".format(quantity_sold, gst_collected, product_code)
                cur=con.cursor()
                cur.execute(v)
                con.commit()
                print_bill(bill_no)
                print()
            print()
            print("Invoice Generated")
            print()
def search_bill():
    t=0
    bill_no=int(input("Enter the Bill Number which you want to Search for: "))
    mycursor=con.cursor()
    mycursor.execute("select * from billing where bill_number={}".format(bill_no))
    myresult=mycursor.fetchall()
    for x in myresult:
        print ()
        print("Bill Number: ", x[0])
        print("Customer Name: ", x[3])
        print("Mobile Number: ", x[4])
        print("Date: ", x[2])
        print()
        break
    p="select serial_no from billing where bill_number={}".format(bill no)
    mycursor.execute(p)
    record=mycursor.fetchall()
    for i in record:
        for j in i:
            s="select * from billing where serial_no='{}'".format(j)
            cur=con.cursor()
            cur.execute(s)
            rec=cur.fetchall()
            for x in rec:
                print("Serial Number: ", i[-1][-1])
                print("Product Name: ", x[5])
                print("Product ID: "‚ x[6])
                print("Price Per Unit: ", x[7])
                print("Quantity: ", x[8])
                print("SGST: ", x[9])
                print("CGST: ", x[10])
                print("Total ", x[11])
                t = t + x[11]
                print()
    print("Grand Total: ", t)
    print("Do you want to print the Invoice?")
    ch=input("Please enter your choice (Y/N): ")
    if ch=="Y":
        print_bill(bill_no)
        print()
        print("Invoice Generated")
        print()
    else:
        print()
        pass()
def search_name():
    t=0
    i=input("Enter the Customer Name which you want to Search for: ")
    mycursor=con.cursor()
    mycursor.execute("select * from billing where customer_name='{}'".format(i))
    myresult=mycursor.fetchall()
    for y in myresult:
        print ()
        print("Bill Number: ", y[0])
        print("Customer Name: ", y[3])
        print("Mobile Number: ", y[4])
        print("Date: ", y[2])
        print()
        break
    p="select serial_no from billing where customer_name='{}'".format(i)
    mycursor.execute(p)
    record=mycursor.fetchall()
    for i in record:
        for j in i:
            s="select * from billing where serial_no='{}'".format(j)
            cur=con.cursor()
            cur.execute(s)
            rec=cur.fetchall()
            for x in rec:
                print("Serial Number: ", i[-1][-1])
                print("Product Name: ", x[5])
                print("Product ID: "‚ x[6])
                print("Price Per Unit: ", x[7])
                print("Quantity: ", x[8])
                print("SGST: ", x[9])
                print("CGST: ", x[10])
                print("Total ", x[11])
                t = t + x[11]
                print()
    print("Grand Total: ", t)
    print()
def search_mobile():
    t=0
    i=input("Enter the Mobile Number which you want to Search for: ")
    mycursor=con.cursor()
    mycursor.execute("select * from billing where mobile_number='{}'".format(i))
    myresult=mycursor.fetchall()
    for x in myresult:
        print ()
        print("Bill Number: ", x[0])
        print("Customer Name: ", x[3])
        print("Mobile Number: ", x[4])
        print("Date: ", x[2])
        print()
        break
    p="select serial_no from billing where mobile_number='{}'".format(i)
    mycursor.execute(p)
    record=mycursor.fetchall()
    for i in record:
        for j in i:
            s="select * from billing where serial_no='{}'".format(j)
            cur=con.cursor()
            cur.execute(s)
            rec=cur.fetchall()
            for x in rec:
                print("Serial Number: ", i[-1][-1])
                print("Product Name: ", x[5])
                print("Product ID: "‚ x[6])
                print("Price Per Unit: ", x[7])
                print("Quantity: ", x[8])
                print("SGST: ", x[9])
                print("CGST: ", x[10])
                print("Total ", x[11])
                t = t + x[11]
                print()
    print("Grand Total: ", t)
    print()
def search_dob():
    t=0
    i=input("Enter the Date of Billing which you want to Search for: ")
    mycursor=con.cursor()
    mycursor.execute("select * from billing where date='{}'".format(i))
    myresult=mycursor.fetchall()
    for x in myresult:
        print()
        print("Bill Number: ", x[0])
        print("Customer Name: ", x[3])
        print("Mobile Number: ", x[4])
        print("Date: ", x[2])
        print()
        break
    p="select serial_no from billing where date='{}'".format(i)
    mycursor.execute(p)
    record=mycursor.fetchall()
    for i in record:
        for j in i:
            s="select * from billing where serial_no='{}'".format(j)
            cur=con.cursor()
            cur.execute(s)
            rec=cur.fetchall()
            for x in rec:
                print("Serial Number: ", i[-1][-1])
                print("Product Name: ", x[5])
                print("Product ID: "‚ x[6])
                print("Price Per Unit: ", x[7])
                print("Quantity: ", x[8])
                print("SGST: ", x[9])
                print("CGST: ", x[10])
                print("Total ", x[11])
                t = t + x[11]
                print()
    print("Grand Total: ", t)
    print()
def search_item():
    t=0
    i=input("Enter the Name of the Item which you want to Search for: ")
    mycursor=con.cursor()
    mycursor.execute("select * from billing where product_name='{}'".format(i))
    myresult=mycursor.fetchall()
    for x in myresult:
        print()
        print("Bill Number: ", x[0])
        print("Customer Name: ", x[3])
        print("Mobile Number: ", x[4])
        print("Date: ", x[2])
        print("Quantity: ", x[8])
        print()
        break
def search_data():
    while True:
        print("1) Search by Bill Number\n2) Search by Customer Name\n3) Search by Mobile Number\n4) Search by Date of Billing\n5) Search by Item\n6) Exit")
        print()
        ch=int(input("Enter your Choice: "))
        if ch==1:
            search_bill()
        elif ch==2:
            search_name()
        elif ch==3
            search_mobile()
        elif ch==4:
            search_dob()
        elif ch==5:
            search_item()
        elif ch==6:
            break
        else:
            print()
            print( "Invalid Choice...")
            print()
            print("Try Again")
            print()

def print_bill(bill_no):
    import csv
    l='select date_format(date, "%d-%m-%y") from billing where bill_number={}'.format(bill_no) 
    cur=con.cursor()
    cur.execute(l)
    rec=cur.fetchall()
    data=[["","","","","Store Name","","",""],["","","","","Invoice","","",""],["","Address Line 1","","","","","","Date",*rec[0]],["","Address Line 2","","","","","","Invoice #",bill_no],["","Phone:","Phone Number","","","",], []]
    filename = str(bill_no)+".csv"
    with open(filename, 'w', newline="") as csvfile:
        csvwriter=csv.writer(csvfile) 
        csvwriter.writerows(data)
    p="select serial_no from billing where bill_number={}".format(bill_no)
    cur.execute(p)
    record=cur.fetchall()
    for i in record:
        for j in i
            s=("select * from billing where serial_no='{}'".format(j))
            cur=con.cursor()
            cur.execute(s)
            rec=cur.fetchall() 
            for r in rec:
                c_name=r[3]
                mob=r[4]
                data=[["","Bill To: ","","","",],["","Customer Name:",c_name,"","",""],["","Mobile No :",mob,"","",],[],["","S. No.","Product Name","Product Code","Price per Unit","SGST","CGST","Quantity","Total"]]
    with open(filename,'a',newline="") as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(data)
        t=0
        for i in record:
            for j in i
                s=('select*from billing where serial_no="{}"' .format(j))
                cur=con.cursor()
                cur.execute(s)
                rec=cur.fetchall()
                for r in rec:
                    s_no=i[-1][-1]
                    p_name=r[5]
                    p_code=r[6]
                    ppu=r[7]
                    qty=r[8]
                    sgst=r[9]
                    cgst=r[10]
                    total=r[11]
                    t=t+total
                    data=["",s_no,p_name,p_code,ppu,sgst,cgst,qty,total]
    with open(filename,'a',newline="") as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(data)
        data=[[],["","Grand Total: ","","","","","","",t,"","","",],[],["","","Thank you for shopping!","","",]]
    with open(filename,'a',newline="") as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(data)
def check_products():
    n=input("Enter the Product Name: ")
    mycursor=con.cursor()
    mycursor.execute("select * from products where product_name='{}'".format(n)) 
    myresult = mycursor.fetchall() 
    for x in myresult:
        print("Serial Number: ", x[0])
        print("Product Name: ", x[2]) 
        print("Product ID: ", x[1])
        print("Price Per Unit: ", x[3])
        print("SGST: ", x[4])
        print("CGST: ", x[5])
        print("Quantity Sold: ", x[6]) 
        print("Stock Remaining: ", x[7])
        print() 
        return
def add_products():
    i=input("Enter the Product ID: ")
    n=input("Enter the Product Name: ") 
    ppu=int(input("Enter the Price Per Unit: "))
    t=float(input("Enter the Tax Rate: "))
    gst=t*ppu
    sc=gst/2
    st=int(input("Enter the Stock: "))
    qty=0
    s="insert into products (product_id, product_name, price per unit, sgst, cgst, stock, quantity_sold) values ('{}','{}',{},{},{},{},{})".format(i,n,ppu,sc,sc,st,qty)
    mycursor=con.cursor()
    mycursor.execute(s)
    con.commit()
    n="insert into due_taxes (product_id, gst_per_product) values ('{}',{})".format(i,gst)
    mycursor.execute(n)
    con.commit()
    u="update due_taxes set quantity_sold=0, gst_collected=0, status='due' where product_id='{}'".format(i)
    mycursor.execute(u)
    con.commit() 
    print()
def update_products():
    i=input("Enter the Product ID which you want to Modify: ")
    d=input("Enter the Updated Product ID: ")
    n=input("Enter the Updated Product Name: ")
    ppu=int(input("Enter the Updated Price Per Unit: "))
    t=float(input("Enter the Updated Tax Rate: "))
    q=int(input("Enter the Updated Quantity Sold: ")) 
    gst=t*ppu
    y="update due_taxes set Product_id='{}', gst_per_product={}, quantity_sold={} where product_id='{}'".format(d,gst,q,i) 
    mycursor =con.cursor()
    mycursor.execute(y) 
    con.commit()
    sc = gst/2
    st=int(input("Enter the Updated Stock: ")) 
    s="update products set product_id='{}', product_name='{}', price_per_unit={}, sgst={}, cgst={}, quantity_sold={}, stock={} where product_id='{}'".format(d,n,ppu,sc,sc,q,st,i) 
    mycursor.execute(s)
    con.commit()
    print()
def check_stock(): 
    i=input("Enter the Product ID for which you want to check the stock: "
    s="select * from products where product_id='{}'".format(i)
    print()
    mycursor=con.cursor()
    mycursor.execute(s)
    myresult=mycursor.fetchall()
    for x in myresult:
        print("Serial Number: ", x[0]) 
        print("Product Name: ", x[2]) 
        print("Price Per Unit: ", x[3]) 
        print("SGST: ", x[4])

def check_taxes():
  i="select product_id,quantity_sold,gst_collected,status from due_taxes"
  mycursor=con.cursor()
  mycursor.execute(i)
  myresult=mycursor.fetchall()
  for a in myresult:
    y="select product_name from products where product_id='{}'".format(a[0])
    mycursor.execute(y)
    myres=mycursor.fetchall()
    print("Product Name: ",*myres[0])
    print("Quantity Sold: ",a[1])
    print("GST_collected: ",a[2])
    print("Status:-",a[3])
    print()
    print()
def pay_taxes():
    total_gst=0
    i="select gst_collected from due_taxes"
    mycursor=con.cursor()
    mycursor.execute(i)
    myresult=mycursor.fetchall()
    for a in myresult:
        for x in a:
            total_gst=total_gst+x
            print("Total GST due:-",total_gst)
            ch=input("Would you like to pay the taxes (Y/N): ")
            if ch=="Y":
                t="update due_taxes set status='Paid', quantity_sold=0, gst_collected=0"
                mycursor.execute(t)
                con.commit()
                print()
def update_gst():
    s=input("Enter the Product Code: ")
    t=float(input("Enter the Updated tax rate: "))
    y="select price_per_unit from products where product_id='{}'".format(s)
    mysursor=con.cursor()
    mycursor.execute(y)
    myresult=mycursor.fetchone()
    x=int(*myresult)
    gst=t*x
    i="update due_taxes set gst_per_product={} where product_id='{}'".format(gst, s)
    mycursor.execute(i)
    con.commit()
    e="select sgst, cgst from products where product_id='{}'".format(s)
    mycursor.execute(e)
    myres=mycursor.fetchone()
    for x in myres:
        x=gst/2
        o="update products set sgst={}, cgst={} where product_id='{}'".format(x, x, s)
        mycursor.execute(o)
        con.commit()
        print("\nGST Updated")
        print()
def bill_management():
    while True:
        print("1) Add Bill\n2) Search Bill\n3)Print Invoice\n4) Exit")
        ch=int(input("Enter Choice: "))
        print()
        if ch==1:
            add_data()
        elif ch==2:
            search_data()
        elif ch==3:
            bill_no=int(input("Enetr Bill Number: "))
            print_bill(bill_no)
            print("Invoice Generated")
        elif ch==4:
            break
        else:
            print("Invalid Choice")
            print("Try Again")
            print()
def tax_management():
    while True:
        print("1) Check Taxes\n2) Pay Taxes\n3) Update GST\n4) Exit")
        ch=int(input("Enter Your Choice: "))
        if ch==1:
            check_taxes()
        elif ch==2:
            pay_taxes()
        elif ch==3:
            update_gst()
        elif ch==4:
            break
        else:
            print("Invalid Choice")
            print("Try Again")
            print()
def product_management():
    while True:
        print("1) Check Products\n2) Add Product\n3) Update Products\n4) Check Stock\n5) Update Stock\n6) Update MRP\n7) Exit")
        ch=int(input("Enter Choice: "))
        print()
        if ch==1:
            check_products()
        elif ch==2:
            add_products()
        elif ch==3:
            update_products()
        elif ch==4:
            check_stock()
        elif ch==5:
            update_stock()
        elif ch==6:
            update_mrp()
        elif ch==7:
            break
        else:
            print("Invalid Choice")
            print("Try Again")
            print()
#MAIN
    while True:
        print()
        print("Welcome to Store Name")
        print()
        print("What do you want to do?")
        print()
        print("1) Bill Management")
        print("2) Taxes Management")
        print("3) Product Management")
        print("4) Exit")
        print()
        ch=int(input("Enter Your Choice: "))
        print()
        if ch==1:
            bill_management()
        elif ch==2:
            tax_management()
        elif ch==3:
            product_management()
        elif ch==4:
            print("Thank you for using our services!")
            break
        else:
            print("Invalid Choicce")
            print("Try Again")
            print()


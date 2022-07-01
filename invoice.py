import csv
import itertools
import datetime
import pandas as pd

class Address:
    def __init__ (self, street: str, city: str, state: str, country: str, pincode: str):
         self.street = street
         self.city = city
         self.state = state
         self.country = country
         self.pincode = pincode


#Customer class holds the details of customer
class Customer(Address):
    def __init__ (self, name: str, address: str, salesTax: float):
        self.name = name
        self.address = address
        self.salesTax = salesTax


#Product class holds the details of each product
class Product:
    def __init__(self, productID: int, name: str, description: str, price: int):
        self.name = name
        self.productID = productID
        self.price = price 
        self.description = description
    
    def inventoryLookup():
        with open('products.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            product_rows = list(csv_reader)
            csv_file.close()
        
        #Printing the product name and quantity remaining in inventory.
        for i in product_rows:
            print(i[1]+" "+i[4])
        return 0

    def get_lowerStockItems():
        with open('products.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            product_rows = list(csv_reader)
            csv_file.close()

        dd=[]
        for i in product_rows[1:]:
            if(int(i[4])<10):
                dd.append("ID"+i[0]+" "+i[1]+" "+i[4]+" needs to be restock")

        return dd

    def inventorylookup_by_id(a):
        with open('products.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            product_rows = list(csv_reader)
            csv_file.close()
        dd=[]
        '''

        if(a!=None and len(a)==1 and type(a)==str and (32<=ord(a)<=47 or 58<=ord(a)<=64 or 91<=ord(a)<=96 or 123<=ord(a)<=126)):
            print("Id will not be a special character,,,, Invalid")
            return -1
        '''    

        if (a==None):
            print("\n Id Input is null")
            return dd

        if(type(a)==str):
            print("Id Input is given as String, Invalid")
            return 'true'        
                
        for i in product_rows[1:]:
                if(int(i[0])==a):
                    dummy_string=i[0]+" "+i[1]+" "+i[2]
                    dd.append(dummy_string)
        print(dd)            
        return dd   

    def inventoryLookup_by_name(a):
        with open('products.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            product_rows = list(csv_reader)
            csv_file.close()
        dd=[]
        
        '''
        if(32<=ord(a)<=47 or 58<=ord(a)<=64 or 91<=ord(a)<=96 or 123<=ord(a)<=126):
            print("Input string is a special character")
            return -1
        '''    
        if(type(a)==str and a!=None and len(a)==1 and (32<=ord(a)<=47 or 58<=ord(a)<=64 or 91<=ord(a)<=96 or 123<=ord(a)<=126)):
            print("Input string is a special character... Invalid")
            return -1

        if (a==None):
            print("\n string Input is null, needs to be string")
            return dd
        if(type(a)==int):
            print("\n string Input is Integer, needs to be string")
            return 'int'

        for i in product_rows[1:]:
            if(a==i[1]):
                dummy_string=i[0]+" "+i[1]+" "+i[2]
                dd.append(dummy_string)
        if(dd==[]):
            print("String not present in products")   
            return 'false'
        print(dd)         
        return dd        

                    



#Invoice class holds the methods for generating invoice
class Invoice(Customer,Product):
    
    def __init__(self, customer: Customer, product: Product, delivery: int):
        self.customer = customer
        self.product = product
        self.delivery = delivery
    
#The function that generates the invoice and stored it in invoices.csv
    def generateInvoice(self):
        if(self.customer.name=="" and self.customer.address=="" and self.delivery==None or self.product.name=="" and self.product.price==None and self.customer.salesTax == None):
            print("entered this ")
            print("invalid input....allinfromation is all empty try again!!")
            return ""

        if((isinstance(self.customer.name, str))== False or (isinstance(self.customer.address, str))== False or (isinstance(self.delivery, int))== False or (isinstance(self.product.name, str)) == False or (isinstance(self.product.price, int)) == False or (isinstance(self.customer.salesTax, int))):
            print("not entered this")
            print("invalid datatypes of the input... please try again!!")
            return ""    






        #reading the number of entries in the file to get the count of invoices
        with open('invoices.csv', 'r') as csvfile:
            csvwriter = csv.reader(csvfile)
            newid = sum(1 for row in csvfile)
            csvfile.close()
        #creating a list which contains all the details of the invoice
        row = [newid,self.customer.name,self.product.name,(self.product.price)+(self.product.price)*(self.customer.salesTax),self.customer.address,(self.delivery)*10,datetime.datetime.now().strftime("%x")]
        #writing this list to the csv
        with open('invoices.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)
            csvfile.close()
            print("Invoice Generated")
        #finally decrementing the quantity of product from products.csv
        df = pd.read_csv("products.csv")
        df.loc[self.product.productID - 1,"quantity"] = int(df.loc[self.product.productID - 1,"quantity"]) - 1
        df.to_csv("products.csv", index=False)
        return row

            
#Driver code to initiate the operations
if __name__ == "__main__":
    input1 = int(input("Select any option from below:: \n 1. Generate Invoice \n 2. Inventory Lookup \n 3. get_lowerStockItems \n 4. Inventory Lookup by id\n 5. Inventory lookup by name---> "))
    if input1 == 1:
        while True:
            try:
                cust1 = int(input("Enter Customer ID:: "))
                if type(cust1) != int:
                    raise ValueError 
                break
            except ValueError:
                print("Invalid input. Please enter only integer.")
                
        while True:
            try:
                prod1 = int(input("Enter Product ID:: "))
                if type(prod1) != int:
                    raise ValueError 
                break
            except ValueError:
                print("Invalid input. Please enter only integer.")
                
        while True:
            try:
                i = int(input("delivery:: "))
                if i < 0 or i > 1:
                    raise ValueError 
                break
            except ValueError:
                print("Invalid integer. Enter 0 for non-delivery or 1 for delivery.")



        with open('customers.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            cust_rows = list(csv_reader)
            csv_file.close()
        with open('products.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            product_rows = list(csv_reader)
            csv_file.close()


        cust1 = Customer(cust_rows[cust1][1],cust_rows[cust1][2],float(cust_rows[cust1][3]))
        prod1 = Product(int(product_rows[prod1][0]),product_rows[prod1][1],product_rows[prod1][2],int(product_rows[prod1][3]))

        inv1 = Invoice(cust1,prod1,i)
        inv1.generateInvoice()

    elif  input1 ==2:
        Product.inventoryLookup()

    elif input1==3:
        dd=[]
        dd=Product.get_lowerStockItems()
        for i in dd:
            print(i)
    elif input1==4:
        id_input=int(input("Enter the ID of the product for lookup: "))
        dd=Product.inventorylookup_by_id(id_input)
        if(dd==[]):
            print("Invalid id")
        print(dd)
    elif input1==5:
        id_input=str(input("Enter the name of the product for lookup: "))
        dd=Product.inventoryLookup_by_name(id_input)

    else:
        print("Enter valid input and try again!!")









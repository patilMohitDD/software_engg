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
            
        for i in product_rows:
            print(i[1]+" "+i[4])
        return 0

    def get_lowerStockItems():
        with open('products.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            product_rows = list(csv_reader)
            csv_file.close()
            
        for i in product_rows:
            if(i[4]<5):
                print(i[1]+" "+i[4])
        return 0
#Invoice class holds the methods for generating invoice
class Invoice(Customer,Product):
    
    def __init__(self, customer: Customer, product: Product, delivery: int):
        self.customer = customer
        self.product = product
        self.delivery = delivery
    
#The function that generates the invoice and stored it in invoices.csv
    def generateInvoice(self):
        if(self.customer.name=="" or self.customer.address=="" or self.delivery==None or self.product.name=="" or self.product.price==None or self.customer.salesTax == None):
            print("invalid input please try again!!")
            return ""
        if((isinstance(self.customer.name, str))== False or (isinstance(self.customer.address, str))== False or (isinstance(self.delivery, int))== False or (isinstance(self.product.name, str)) == False or (isinstance(self.product.price, int)) == False or (isinstance(self.customer.salesTax, int))):
            print("invalid input please try again!!")
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
    input1 = int(input("Select any option from below:: \n 1. Generate Invoice \n 2. Inventory Lookup \n ---> "))
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
    else:
        print("Enter valid input and try again!!")
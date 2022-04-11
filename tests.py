import unittest
import invoice

class TestMethods(unittest.TestCase):

    def test_invoicenull(self):
        cust =  invoice.Customer("", "", 0)
        prod =  invoice.Product(0, "", "", 0)
        inv =  invoice.Invoice(cust, prod, 0)
        inv.generateInvoice()
    
    def test_invoicenormal(self):
        cust =  invoice.Customer("Arjang Fahim", "1250 Bellflower Blvd", 0.10)
        prod =  invoice.Product(1, "TV1", "This is a TV1", 40)
        inv =  invoice.Invoice(cust, prod, 0)
        print(inv.generateInvoice())

    def test_invoicetypecheck(self):
        cust =  invoice.Customer(12, 23, "none")
        prod =  invoice.Product(1, "TV1", "This is a TV1", 40)
        inv =  invoice.Invoice(cust, prod, 0)
        print(inv.generateInvoice())
        
        
        
if __name__ == '__main__':
    unittest.main()
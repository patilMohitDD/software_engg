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

    def test_get_lowerstockitems_lookup_for_refill_stocks(self):
        dd=invoice.Product.get_lowerStockItems()
        ###creating a list to get the id's of the stocks which aare need to be refill
        dd1=[]
        for i in dd:
            dd1.append(i[2])
        self.assertCountEqual(dd1,['1','2'])

    def test_inventorylookup_by_id_if_id_outofbound(self):
        dd=invoice.Product.inventorylookup_by_id(6)
        self.assertCountEqual(dd,[])

    def test_inventorylookup_by_id_if_id_null(self):
        dd=invoice.Product.inventorylookup_by_id(None)
        self.assertTrue(dd,"")    

        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)







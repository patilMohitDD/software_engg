import unittest
import invoice

class TestMethods(unittest.TestCase):
    '''
    ## Test case for checking all the infromation in input is nothing
    def test_invoicenull(self):
        cust =  invoice.Customer("", "", 0)
        prod =  invoice.Product(0, "", "", 0)
        inv =  invoice.Invoice(cust, prod, 0)
        self.assertEqual(inv.generateInvoice(),"")
    
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
    '''    



    ## Get lower stock items to check test case
    def test_get_lowerstockitems_lookup_for_refill_stocks(self):
        dd=invoice.Product.get_lowerStockItems()
        ###creating a list to get the id's of the stocks which aare need to be refill
        dd1=[]
        for i in dd:
            dd1.append(i[2])
        self.assertCountEqual(dd1,['1','2'])


    ## Test case for inventory lookup by id, if input is out of bound 
    def test_inventorylookup_by_id_if_id_outofbound(self):
        dd=invoice.Product.inventorylookup_by_id(6)
        self.assertCountEqual(dd,[])

    ## Test case for inventory lookup by id, if input is none/empty/nothing 
    def test_inventorylookup_by_id_if_id_null(self):
        dd=invoice.Product.inventorylookup_by_id(None)
        self.assertEqual(len(dd),0)

    ## Test case for inventory lookup by id, if input is wihtin bounds
    def test_inventorylookup_by_id_if_id_is_within_bound(self):
        dd=invoice.Product.inventorylookup_by_id(2)
        dd_1=['2 TV2 Description of TV2']
        self.assertEqual(dd,dd_1)

    ##Test case for inventory lookup by id, if input is string 
    def test_inventorylookup_by_id_if_id_is_givenas_string(self):
        dd=invoice.Product.inventorylookup_by_id("hello")
        self.assertEqual(dd,'true')
'''
    ## Test case for inventory lookup by id, id input is a single special character
    def test_inventorylookup_by_id_if_id_is_givenas_specialcharacter(self):
        dd=invoice.Product.inventorylookup_by_id('@')
        self.assertEqual(dd,-1)

'''



    ## test case for inventory lookup by name of the product, input is none/empty/nothing
    def test_inventorylookup_by_name_if_name_is_empty(self):
        dd=invoice.Product.inventoryLookup_by_name(None)
        self.assertEqual(len(dd),0)

    ## test case for inventory lookup by name of the product, input is integer
    def test_inventorylookup_by_name_if_name_is_integer(self):
        dd=invoice.Product.inventoryLookup_by_name(2)
        self.assertEqual(dd,'int')   

    ## test case for inventory lookup by name of the product, input is string(present)
    def test_inventorylookup_by_name_if_name_is_string_present(self):
        dd=invoice.Product.inventoryLookup_by_name('Stereo1')
        dd_1=['3 Stereo1 Description of Stereo1']
        self.assertEqual(dd,dd_1)

    ## test case for inventory lookup by name of the product, input is string(absent)
    def test_inventorylookup_by_name_if_name_is_string_absent(self):
        dd=invoice.Product.inventoryLookup_by_name('anything')
        self.assertEqual(dd,'false')

    
    ## Test case for inventory lookup by name of the product, input is string(special character) 
    def test_inventorylookup_by_name_if_name_is_string_specialcharacter(self):
        dd=invoice.Product.inventoryLookup_by_name('@')
        self.assertEqual(dd,-1)

    


 
if __name__ == '__main__':
    unittest.main(verbosity=2)







from abc import ABC,abstractmethod
from ecom_application.entities import Product
import random

REVIEWS = ["1*","2*","3*","4*","5*"]
MANUFACTUING = []
for item in range(10):
    MANUFACTUING.append(Product(pid=item+1,pnm="XXXX"+str(item),ppri=random.randint(100,500),
                                pqty=random.randint(10,50),prev=REVIEWS[random.randint(0,4)]))






class VendorService(ABC):

    @abstractmethod
    def import_products(self,pname,ven):
        pass


import copy

class VenodrServiceImpl(VendorService):
    MIN_REQUIRED_BAL = 5000.0

    def import_products(self,prodName,pqty,vendor):  #p1--> 2
        productfound = False
        for stockproduct in MANUFACTUING:    #company [p1:10,p2:3,p3:10,p4:8,P5:7]
            if stockproduct.productName == prodName:
                productfound = True
                if stockproduct.productQty >= pqty:

                    totalBill = pqty*stockproduct.productPrice
                    print("Total Bill-->", totalBill)
                    if totalBill+VenodrServiceImpl.MIN_REQUIRED_BAL<=vendor.venAccount.accBal:
                        venproduct = copy.deepcopy(stockproduct)  #stock-->p1:10  custprod-->p1:10
                        venproduct.productQty=pqty   #custprod --> 2
                        stockproduct.productQty = stockproduct.productQty - pqty #stockproduct : 8
                        vendor.venInventory.append(venproduct) #
                        vendor.venAccount.accBal = vendor.venAccount.accBal - totalBill
                        print(vendor.venName,",Given Products -->",vendor.venInventory)
                    else:
                        print('Insufficient Balance..!')
                else:
                    print('Insufficient Qty..>!')
                break

        if not productfound:
            print('Product Not Available..!')

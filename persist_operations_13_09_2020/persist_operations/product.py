class Product:

    def __init__(self,pid,pnm,prc,pqty,prem):

        self.prodId = int(pid)
        self.prodName = pnm
        self.prodPrice = float(prc)
        self.prodQty = int(pqty)
        self.prodRemarks = prem

    def __str__(self):
        return f''' ({self.prodId},{self.prodName},{self.prodQty},{self.prodPrice},{self.prodRemarks})'''

    def __repr__(self):
        return str(self)

    def __eq__(self, other):  # for content equality --- how does products are same in my case--> based id contents
        return self.prodId == other.prodId



# queries -->
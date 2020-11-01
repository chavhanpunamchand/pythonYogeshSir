

#what is product means --> user defined structure--> product type
class Product:

    def __init__(self,pid,pnm,prc,pqt,pbar):
        self.prodId = int(pid)
        self.prodName = pnm
        self.prodPrice = float(prc)
        self.prodQty = int(pqt)
        self.prodBarcode = pbar

    def __str__(self):
        return f'''[{self.prodId},{self.prodName},{self.prodPrice},{self.prodQty},{self.prodBarcode}]'''

    def __repr__(self):
        return str(self)

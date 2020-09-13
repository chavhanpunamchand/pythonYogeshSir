
#window --> linux ->
FILE_PATH = 'C:/Users/Yogesh/PycharmProjects/persist_operations/weekend_2'
#FILE_PATH = 'C:\\Users\\Yogesh\\PycharmProjects\\nnersist_operations\\weekend_2'
import openpyxl
#EXCELSHEET --> WORKBOOK --> SHEETS --> ROWS - COLUMNS

class InvalidProductParam(BaseException):

    def __init__(self,msg,*args,**kwargs):
            self.errormessage = msg

class Product:
    def __init__(self,pid,pnm,prc,pqty,pbar):
        self.prodId = pid
        self.prodName = pnm
        self.prodQty = pqty
        self.prodPrice = prc
        self.prodBarCode = pbar

    def __str__(self):
        return f'''{self.prodId},{self.prodName},{self.prodPrice},{self.prodQty},{self.prodBarCode}'''

    def __repr__(self):
        return str(self)









class InvalidProductId(BaseException):
    def __init__(self, msg, *args, **kwargs):
        self.message = msg

class InvalidProductPrice(BaseException):
    def __init__(self,msg,*args,**kwargs):
        self.message = msg


def get_input_id_price():
    try:
        pid = int(input('Enter Product Id : '))     #("invalid literal for int() with base 10: 'nnn'",)
    except ValueError as v:
        raise InvalidProductId("Product Id should be Numeric - Integer value")  # whoever calls to

    try:
        prc = float(input('Enter Product Price : '))
    except ValueError as v:
        raise InvalidProductPrice("Product Price should be Numeric/decimal - Integer/float value")

    return pid,prc          # in case no raise..


if __name__ == '__main__':
    while True:  # even though its while--> in case excepit
        try:
            pid,prc = get_input_id_price()  # risky line--> might run -- may not be
            a = 1000/pid    #  can this be
            print('Valid INputs -->',pid,prc)
        except InvalidProductId as e:
            print(e.message)    # IN CASE ID IS INVALID--> THEN--> YOU CAN WRITE UR LOGIC
        except InvalidProductPrice as e:
            print(e.message)    # IN CASE ID IS PRICE--> THEN--> YOU CAN WRITE UR LOGIC

        except BaseException as b:       #same or any parent --> of ZeroDivisionError --> direct or indirect
            print(type(b))
            print('Problem in product create..')
        #except BaseException as e:
        #    print(type(e))  # next type-> tyacha--> except  ---> mature --> 3 4 --> over the years
        #    print(e.message)





import sys
sys.exit(0)
def get_input_from_user():
    try:
        pid = int(input('Enter Product Id : '))
        pnm = input('Enter Product Name :')
        pric = float(input('Enter Product Price :'))
        pqty = int(input('Enter Product Qty : '))
        prodBar = input('Enter Product BarCode : ')
        a = 10/0
    except ValueError as v:
        pass
    except BaseException as e:
        print('Problem in creating product')
    else:
        if pid and pnm and pric and pqty and prodBar:
            return Product(pid,pnm,pric,pqty,prodBar)
        raise InvalidProductParam("Required params are not present...!") #customize-->


def write_data_into_excelsheet():
    workbook = openpyxl.Workbook()
    sheet = workbook.create_sheet('productinfo')
    sheet['C5'] = "Python"
    sheet['C10'] = "lang"
    workbook.save('prod.xlsx')
    print(sheet)


if __name__ == '__main__':
    try:
        product = get_input_from_user()
    except InvalidProductParam as p:
        print(p.errormessage)



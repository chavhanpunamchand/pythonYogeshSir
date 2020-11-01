
def check_proper_pincode(pincode):      #ABCDER     -->string method --> all numbers ??
    pincode = str(pincode)
    if len(pincode)==6 and pincode.isnumeric():
        return True
    return False


    #if type(pincode)==int and pincode>99999 and pincode<1000000:
    #    pass

    #100    000
def check_for_email(email):
    #abc@gmail.com
    values = email.split("@")       # ueyadgagdhsa      abc.com.com
    if len(values)==2 and len(values[0])>=2:
        values = values[1].split(".")  #abc.com.com --> 3
        if len(values)==2 and len(values[0])>=3:
            if len(values[1])>=2:
                return True
    return False


#flag = check_for_email("ueyadgagdhsa@abc.com")
#print("Is Proper email -->" , flag)
#import sys
#sys.exit(0)

def is_proper_account(vacc):
    if not type(vacc) == Account or vacc.accBal<5000.0:
        return False
    return True

def is_proper_address(adr):
    if not type(adr)==Address:
        return False
    return True


class Product:  # who --> developer --> product [id,nm,price,qty,reviews]
    def __init__(self,pid,pnm,ppri,pqty,prev):  # constructor --?  object--> every props-->
        self.productId = pid
        self.productName = pnm
        self.productPrice = ppri
        self.productQty = pqty
        self.productReviews=prev

    def __str__(self):
        return f'''
            Product Id : {self.productId}
            Product Name : {self.productName}
            Product Price : {self.productPrice}
            Product Qty : {self.productQty}
            Product Remarks : {self.productReviews}
        '''

    def __repr__(self):
        return str(self)


    def __eq__(self, other):
        return self.productId == other.productId


class Customer:
    def __init__(self,cid,cnam,cag,cemail,cadr,cacc):
        self.custId = cid
        self.custName = cnam
        self.custAge = cag          # 18
        self.customerEmail = cemail
        self.customerAddress = cadr
        self.customerAcccount  = cacc

    def __str__(self):
        return f'''
            Customer Id : {self.custId}
            Customer Name : {self.custName}
            Customer Age : {self.custAge}
            Customer Email : {self.customerEmail}
            Customer Account Info : {self.customerAcccount.accId},{self.customerAcccount.accType},{self.customerAcccount.accBal}
            Customer Address Info : {self.customerAddress.adrId},{self.customerAddress.city},{self.customerAddress.state},{self.customerAddress.pincode}
        '''

    def __repr__(self):
        return str(self)

    @classmethod  # cls-->Vendor
    def get_customer_instance(cls,cid,cnam,cag,cemail,cadr,cacc):
        flag = True

        if is_proper_account(cacc) == False:
            print("Invalid Account Type or Minimum Balance")
            flag = False

        if not is_proper_address(cadr):
            print('Invalid Address')
            flag = False

        if not check_for_email(cemail):
            print('Invalid Email')
            flag = False

        if flag:
            return cls(cid,cnam,cag,cemail,cadr,cacc)
        else:
            print('Customer Instance cannot be created as Incorrect Params')


class Vendor:

    def __init__(self, regid, vnam, vemail, vadr, vacc):
        self.venRegId = regid
        self.venName = vnam
        self.venEmail = vemail
        self.venAddress= vadr
        self.venAccount = vacc
        self.venInventory = []  # vendor --> Inventory Blank -->
    @classmethod        #cls-->Vendor
    def get_vendor_instance(cls,regid, vnam, vemail, vadr, vacc):
        flag = True

        if is_proper_account(vacc) == False:
           print("Invalid Account Type or Minimum Balance")
           flag = False

        if not is_proper_address(vadr):
            print('Invalid Address')
            flag = False

        if not check_for_email(vemail):
            print('Invalid Email')
            flag=False

        if flag:
            return cls(regid, vnam, vemail, vadr, vacc)
        else:
            print('Vendor Instance cannot be created as Incorrect Params')

    def __str__(self):
        return f'''
            Vendor Id : {self.venRegId} 
            Vendor Name : {self.venName}
            Vendor Email : {self.venEmail}
            Vendor Account Info : {self.venAccount.accId},{self.venAccount.accType},{self.venAccount.accBal}
            Vendor Address Info : {self.venAddress.adrId},{self.venAddress.city},{self.venAddress.state},{self.venAddress.pincode}
            Vendor Inventory  : {self.venInventory}
        '''
            #self.venAccount.accId --> int --
            #self -->vendortype
            #self.venAccount -->AccountType
            #self.venAccount.accId --> account madhla id
            #self.vendorType.venAccount --> ya venchya account madhla id -->

            #Vendor Address : {self.venAddress}  #address str --> print
            #Vendor Account :{self.venAccount}   #account str --> print


    def __repr__(self):
        return str(self)

class Account:
    def __init__(self,acid,acty,acbal):
        self.accId = acid
        self.accType = acty
        self.accBal = acbal

    def __str__(self):
        return f'''
            Account Number : {self.accId}
            Account Type : {self.accType}
            Account Balance : {self.accBal}
        '''

    def __repr__(self):
        return str(self)


    def __eq__(self, other):
        return self.accId == other.accId

class Address:
    def __init__(self,adrid,city,state,pin):
        self.adrId = adrid
        self.city = city
        self.state = state
        self.pincode = pin

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''
            City : {self.city}
            State : {self.state}
            Pincode : {self.pincode}
        '''
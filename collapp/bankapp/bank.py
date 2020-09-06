





def m1(a,b=33,c=111):
    print(a)
    print(b)
    print(c)

m1(10,20,30) #cannot say
m1(100) #not possible thru positional --> seq
m1(a=100,c=222) # # only using named params



class Bank:

    def __init__(self,bid,bnm,bifsc,badr="Pune"):  # to initi obj props
        self.bankId  = bid
        self.bankName = bnm
        self.bankAddress= badr
        self.bankISFCCode= bifsc

    def __str__(self):               # for obj display
        return f'''
                Bank Id : {self.bankId}
                Bank Name : {self.bankName}
                Bank Address : {self.bankAddress}
                Bank ISFC : {self.bankISFCCode}
        '''#.format(self.bankId,self.bankName,self.bankAddress,self.bankISFCCode)

b1 = Bank(101,"HDFC","HDFC00076","Pune")        #positional
b2 = Bank(101,"HDFC","HDFC00076") #will work --> here default address would be punt
b3 = Bank(badr="Mumbai",bid=102,bifsc="SBI00012",bnm="SBI")#named
b4 = Bank(bid=102,bifsc="SBI00012",bnm="SBI")#named # default address would be pune




#positional --> position--seq matters--> cannot change seq-->  if changed--> param-interchange -> no of param -yes
#named --> name matters --> seq doesnt matter-->    no of param -> Yes
#default param --> optional params *--> no of params doent matter--> make sure-- default params-- shud be at last--

# m1 --- 10 params -->      3 params default    --->        mandatory -> 7      --> 7 8 9 10


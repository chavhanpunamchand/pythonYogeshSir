

class Product:

    def __init__(self,pid,pnm,pri,pqty,pbar):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = pri
        self.prodQty = pqty
        self.prodCode = pbar

    def __repr__(self):
        return str(self)

    def __str__(self):                      #self -- current object ref--       self.__dict__   --> {prodId:101,}
        prodcontents = ''       #create dynamic-- string- based on object properties
        for propname,propvalue in self.__dict__.items():
            prodcontents = "\n"+prodcontents + propname +":" +str(propvalue)+"\n"
        return prodcontents     # all properties-- with thr values--\n

#str class python-->  check all method once -->

#num = 10         #int
#num = str(num)  #str
#num = num+"A"   #10A    --
#if num.isnumeric(): # string-- numeric asel tr-- int madhe convert kr-->
#    num  = int(num) #int    --error

products = []
for item in range(10):
    p1 = Product(101+item,"AAAA"+str(item),2929.34+item,27+item,'A{}XXX'.format(item))  #python object--> to be converted into json
    products.append(p1.__dict__)

print(products)



# crud --> create --> read -> update -- delete -->
# file-->read/write-->



import json     # python provided-->
                #json.load  --> input-- file type[json] --> object format
                #json.dumps --> dict or list of dict--> json->
prodjson = json.dumps(products)     #

with open('product.json','w') as file:
    file.write(prodjson)                # write that json into file



#json.load()    --> read json file contents give me python object format--dict




#with open('product.json','w') as file:

import sys
exit(0)


class Person:
    def __init__(self,uid,unm,tit,body):
        self.uid = uid       #this is id
        self.userId = unm # this is userId
        self.title = tit        #this is title
        self.body = body        #this is body

    def __str__(self):
        return f'''
                User Id : {self.uid},
                User Name : {self.userId},
                Title : {self.title},
                Body : {self.body},
        '''

    def __repr__(self):
        return str(self)



import json     # module --> implict--> python provided

# char --> to ascii --> ord     --> A   --> ord('A') --> 65 -->     A-Z [65-90]     a-z [97-122]    0-9 [48-57] space[32]
# ascii-- to char ---> chr      --> 65 ---> chr(65) ---> A

#--> first --> json --> python object--> then sorting/searching-->
#file type -> lang format -->  process --> deserilization -->
#python --> file format --> txt/excel/json/csv/xml --> serialization -->

#lang - to file format --> serialaztion
#file to lang -> deser

#load -- accepts file type[json]--> converts it into --> dict format-->

def convert_json_file_contents_to_python_object():  #deserialization
    with open('user.json','r') as file:
        filecontents = json.load(file)
        #print(filecontents)
        persons = []
        users =  filecontents.get("userinfo")
        for user in users:
            per = Person(user.get("id"),user.get("userId"),user.get("title"),user.get("body"))
            persons.append(per)
    return persons


def per_sort_logic(per):    #custom --> object--> on which property u want to sort-->
    return per.uid


def get_ascii(items):
    num = 0
    for item in items:
        num = num+ord(item)
    return num

if __name__ == '__main__':
    #persons = convert_json_file_contents_to_python_object()
    #print('before sort -->',persons)
    #persons.sort(key=per_sort_logic,reverse=True)  # ref to per_sort_logic->         on which property ??? which property ?? --> person ??  user defined ??
    #persons.sort(key = lambda per : per.title,reverse=True)
    #print('after sort -->', persons)

    #values = ["10","23","44","2",34,"A"]    # sorting--> possible in hom data elements--
    #print("before --", values)
    #values.sort(reverse=True)
    #print("after --",values)


    values = [10,2,34,5,67,"A","B","X","AA"] # 10 2 34 5 67 65 66 88
    values.sort(key=lambda item : get_ascii(item) if type(item)==str else item)       #
    print(values)


#def xyz(item):
#    if type(item)==str:
#        return ord(item)
#    else:
#        return item
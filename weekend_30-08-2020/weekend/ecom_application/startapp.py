from ecom_application.entities import *
from ecom_application.service import VenodrServiceImpl,MANUFACTUING

'''
Exception Handling--*-> handle-->
        Looping*

College App -->
        College --> id nm    addr*   dept[]*   Account  *
        Dept -- id code name stud[]* prof[]*
        Student-id name mark* address*  fees   
        Prof    id nm expr skills[] sal         Account*
        Address -- id city state pin 
        marks -- phy chem math
        Account -- id type bal
        
        1. topper -- irrectpective of dept--> college topper --> [phy,chem,math]
                  --> college -- subj -->                   --> subjname --> 
                  --> dept wise -- topper-->                -->dept 
                  -->deptwise --                            -->subj,dept
        2. CollegeExps --> total prof salary --->   
                                annual *12 -->
                                monthly--> 
        3 College Earning --    totalfees - total prof salary
                    #dept wise earning -->      dept student fees - dept prof salary
        
        4   RegionWise Topper -->       PUne --> student scan belongs to pune --> topper
        
        5.  multiple depts --> teaching -- professors   --> max 2dept-> 10% --> increment
                3-4-5 ---> 10%
                5%
        6.  ??


'''





# generic types--> dynamic
if __name__ == '__main__':

    adr1 = Address(adrid=5551,city='Pune',state='MH',pin=112233)
    ac1 = Account(acid=112233, acty="C", acbal=9000.34)
    ven1 = Vendor(regid="V1281", vnam="Flipkart", vemail="flip@flipkart.com", vadr=adr1, vacc=ac1)

    adr2 = Address(adrid=2351, city='Mumbai', state='MH', pin=112233)
    ac2 = Account(acid=442112, acty="S", acbal=40000.34)
    cust1 = Customer.get_customer_instance(cid=1111,cnam='Mr XXXX',cag=34,cemail='abc@gmail.com',cadr=adr2,cacc=ac2)

    print('vendor',ven1)

    MANUFACTUING[9].productQty=10   # [P0,P1,P2,P3,P4,P5,P6,P7,P8,P9:10]
    MANUFACTUING[9].productPrice=1000    #100-->                 5*1000 --> 5000

    print('MANG-->Before -->',MANUFACTUING[9]) #45
    service = VenodrServiceImpl()
    service.import_products("XXXX9",5,ven1)  # flipkart -- order place --> 5 lappys

    print('MANF ->AFTER -->', MANUFACTUING[9]) # 3

    print('vendor',ven1)


    #customer --> order product --> [prodnm,prodqty,cust]   --> cross check --> vendorinventory -->
                                            #nm -- qty -- custbal -->
                                                        #venaccount + totalbil  -- invenotyr prodqty minus
                                                        #custacount-total       --> customer inventory plus
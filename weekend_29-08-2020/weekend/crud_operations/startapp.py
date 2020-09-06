from Basics.weekend.crud_operations.student import Student
from Basics.weekend.crud_operations.service import StudentServiceImpl
#user choice --> switch condition -->
    # 1 --> add student --> enter id enter name enter age enter address-->
                        # id --> num --> wrong --> 3 times --> attempt--
                        #duplicate student
                        #fees --> add one more property     --> id nm age adr -->       fees dept
                        # tell me total fees        --> irrespective dept
                        #dept -->
                                #fees group by deptwise -->     deptwise-->
                        # search by --?address/dept-->name -->id -->contact->email-->dept--->
if __name__ == '__main__':
    s1 = Student(sid=101,snm="Mr. XXXX1",sag =29,sadr='Pune')
    s2 = Student(sid=102, snm="Mr. XXX2X", sag=23, sadr='Pune')
    s3 = Student(sid=103, snm="Mr. X4XXX", sag=24, sadr='Pune')
    s4 = Student(sid=104, snm="Mr. XXX5X", sag=19, sadr='Pune')
    s5 = Student(sid=105, snm="Mr. XX5XX", sag=22, sadr='Pune')

    service = StudentServiceImpl()

    service.add_student(s1)
    service.add_student(s2)
    service.add_student(s3)
    service.add_student(s4)
    service.add_student(s5)
    print("104 -->", service.fetch_single_student(104))
    service.delete_student(104)
    print("104 -->", service.fetch_single_student(104))

    '''
    print('FETCH Single Student -->')
    print("108 -->",service.fetch_single_student(108))
    print("105 -->", service.fetch_single_student(105))

    print('Fetch AllStudents')
    print(service.fetch_all_students())
    
    '''
    '''
    print("105 -->", service.fetch_single_student(104)) #pune

    print('update student -->')
    
    s4.studAddress="Mumbai" # change address-->     memory
    service.update_student(104,s4) #no --> 106 -->      Pune -->mUmbai

    print('after update--')

    print("105 -->", service.fetch_single_student(104))     #mumbai

    print('All -->',service.fetch_all_students())   #mumbai
    '''

def get_student_info():
    with open('student.txt','r') as file:
        return [line.strip() for line in file.readlines()]


class StudentDataIterator:

    def __init__(self,start=0,no=5):
        self.studentdata = get_student_info()    # 65   --> 65
        self.noof = no                      # 5         --> 5
        self.start = start                  # 0         --> 0
        self.end = no                       # 5         --> 5

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.studentdata)>self.end:      #True
            value = self.studentdata[self.start:self.end]   #[0,5] --> no of students in values-- 5
            self.start = self.start + self.noof  #0     5      10
            self.end = self.end + self.noof      #5 --> 10      15
            return value
        else:
            raise BaseException("All Students Processed..")


stud = StudentDataIterator(start=0,no=1)

import time
for no,item in enumerate(stud):
    print(no+1,item)
    time.sleep(1)


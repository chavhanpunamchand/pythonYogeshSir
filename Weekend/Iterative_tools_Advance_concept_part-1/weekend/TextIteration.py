
     # 1inch -->  7 lines -->       --> function -->
class ProcessFile:                  # iterable

    def __init__(self,screensize,start=0,flag='W'):
        with open('sample.txt','r') as file:
            self.flag = flag
            self.alllines = [line.strip() for line in file.readlines()] #294
            self.allwords = [lin.split(" ") for lin in self.alllines]
            self.finalwordlist = []
            for word  in self.allwords:
                self.finalwordlist.extend(word)
            self.screensize = screensize                                #7
            self.start = start

    def __iter__(self):     # will process file instance as --> Iterable
         # 0
        self.nextstop = self.start + self.screensize  # 20
        if self.flag == 'W':
            self.end = len(self.finalwordlist)
        else:
            self.end = len(self.alllines)  # 294

        return self

    def __next__(self):     # write u logic--> to return --> on each iteration
        if self.end > self.nextstop:
            if self.flag=='W':
                lines = self.finalwordlist[self.start:self.nextstop]
            else:
                lines = self.alllines[self.start:self.nextstop]
            self.start = self.start + self.screensize
            self.nextstop = self.nextstop + self.screensize
            print('-------------------------------------------------')
            return lines
        else:
            raise StopIteration("All elements processing completed..")



MOBILE_SCREEN_SIZE = 10
procesfile = ProcessFile(MOBILE_SCREEN_SIZE,start=0,flag='L')
#print(procesfile.finalwordlist)
#import sys
#sys.exit(0)

#print(next(procesitr))      # 0-9--> first 1-10 lines
#print(next(procesitr))      # 10-19--> first 11-20 lines
import time

procesitr = iter(procesfile)


for lin in procesfile:
    print(lin)
    time.sleep(1)


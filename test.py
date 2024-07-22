import time
import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import BaseManager

class Mem:
    def __init__(self):
        self.A1 = float(0) #Manager().Value('f', 0)
        self.B1 = True #Manager().Value('b', True)
    
    def SetA1(self, val):
        self.A1 = val
        
    def GetA1(self):
        return self.A1
        
    def SetB1(self, val):
        self.B1 = val
        
    def GetB1(self):
        return self.B1
        
def test_proc_func2(mem1):
    print(mem1.GetB1())
    while mem1.GetB1:
        #print(999)
        mem1.SetA1(time.time())
        time.sleep(0.1)
        
class CustomManager(BaseManager):
    # nothing
    pass
    
if __name__ == "__main__": 
    processes = []
    CustomManager.register('Mem', Mem)
    print(111)
    #mem2 = Mem();
    with CustomManager() as manager:
        print(222)
        mem1 = manager.Mem()
        print(333)
        proc = Process(target = test_proc_func2, args = [mem1])
        print(444)
        proc.start();

        counter = 0
        while True:
            print(mem1.GetA1())
            time.sleep(1.0)
            counter = counter + 1
            #test_proc_func2(mem2)
            if counter > 30:
                mem1.SetB1(False)
                break
                
        proc.join();
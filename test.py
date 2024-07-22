import time
import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import BaseManager

class Mem:
    def __init__(self):
        self.A1 = float(0) 
        self.A2 = float(0)
        self.B1 = True 
    
    def SetA1(self, val):
        self.A1 = val
        
    def GetA1(self):
        return self.A1
        
    def SetA2(self, val):
        self.A2 = val
        
    def GetA2(self):
        return self.A2
        
    def SetB1(self, val):
        self.B1 = val
        
    def GetB1(self):
        return self.B1
        
def test_proc_func1(mem1):
    print(mem1.GetB1())
    while mem1.GetB1:
        #print(999)
        mem1.SetA1(time.time())
        time.sleep(0.1)
        
def test_proc_func2(mem1):
    print(mem1.GetB1())
    while mem1.GetB1:
        #print(999)
        mem1.SetA2(time.time()-100)
        time.sleep(0.1)
        
class CustomManager(BaseManager):
    # nothing
    pass
    
if __name__ == "__main__": 
    #freeze_support()
    CustomManager.register('Mem', Mem)

    with CustomManager() as manager:

        mem1 = manager.Mem()

        proc = Process(target = test_proc_func1, args = [mem1])
        proc.start();
        
        proc2 = Process(target = test_proc_func2, args = [mem1])
        proc2.start()

        counter = 0
        while True:
            print("A1: ",mem1.GetA1())
            print("A2: ",mem1.GetA2())
            time.sleep(1.0)
            counter = counter + 1
            if counter > 30:
                mem1.SetB1(False)
                break
                
        proc.join();
        proc2.join();
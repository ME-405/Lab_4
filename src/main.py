"""!
     @file       main.py
     @brief      A brief code that manages queues for Lab-4
     @author     Nick De Simone, Jacob-Bograd, Horacio Albarran
     @date       February 08, 2022
"""

# Importing libraries and classes
import pyb
import utime
import micropython
from task_share import Queue

# Setting up pins and variables
pinC1 = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.IN)
myADC = pyb.ADC(pinC0)
micropython.alloc_emergency_exception_buf(100)
que = Queue('h', 2000)

def interrupt(dummy):
    '''!
        @brief   An interrupt function that reads queues and place them in the queue
        @param   dummy is just a dummy variable
    '''
    # read the ADC
    num = myADC.read()
    # put the value in the queue
    if not que.full():
        que.put(num)

def printQue():
    '''!
        @brief  It places the read value onto the queue
    '''
    while not que.empty():
        print(que.get())
    print('DONE')

def pinlow():
	'''!
        @brief  Setting pinC1 to low 
    '''

    pinC1.low()
    utime.sleep_ms(3000)

def main():
	'''!
        @brief  Main running function where a timer interrupt is set
    '''
    
    #start low
    #pinC1.low()
    #utime.sleep_ms(10)
    # make the timer
    timer = pyb.Timer(1)
    # set the callback
    timer.callback(interrupt)
    # start it up
    timer.init(freq=1000)
    #get high
    pinC1.high()
    while not que.full():
        # mine bitcoin I guess
        pass
    timer.callback(None)
    printQue()


## To run the file automatically from putty every time the system resets
if __name__ == '__main__':
    pinlow()
    main()







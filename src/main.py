import pyb
import utime

from task_share import Queue

# setup everything

pinC1 = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.IN)
myADC = pyb.ADC(pinC0)
que = Queue('**h**', 1000)


def interrupt():
    # read the ADC
    num = myADC.READ()
    # put the value in the queue
    if not que.full():
        que.put(num)

def printQue():
    while not que.empty():
        print(que.get())

def main():

    #start low
    pinC1.low()
    utime.sleep_ms(10)
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





if __name__ == '__main__':
    main()

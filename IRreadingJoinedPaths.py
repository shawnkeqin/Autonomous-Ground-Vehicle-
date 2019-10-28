import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)


IO.setup(23,IO.IN) #GPIO 14 -> IR sensor 3 as input
IO.setup(20,IO.IN) #GPIO 14 -> IR sensor 4 as input
IO.setup(55,IO.IN) #GPIO 14 -> ULtrasonic sensor as input


IRreading3 = 0
IRreading4 = 0

#FOr split paths - need to adjust GPIO Pins

while 1:
        IRreading3 = IO.input(23)
        IRreading4 = IO.input(20)
        ultrasonic = IO.input(55)
        
        if(IRreading3== 0 && IRreading4 ==0):
            time.sleep(2)
            if(ultrasonic == 1):
               left()
               print ('drop off')
            elif(ultrasonic == 0):
                right()
                print ('collection')
            

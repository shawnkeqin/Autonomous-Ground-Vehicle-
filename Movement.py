import RPi.GPIO as IO
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
import time 
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.cleanup()
IO.setup(11,IO.IN, pull_up_down = IO.PUD_DOWN)
IO.setup(7,IO.OUT)
IO.output(7,0) #set ping 7 to be 0 at default



#coloursensor
s2 = 22
s3 = 4
signal = 16
NUM_CYCLES = 10

#IO.setup(6,IO.OUT) #GPIO 2 -> Red LED as output
#IO.setup(5,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(20,IO.IN) #GPIO 14 -> IR sensor as input #sensor3black
IO.setup(25,IO.IN)#switch
IO.setup(17,IO.IN) #sensor4white
IO.setup(12,IO.IN) #sensor2white
IO.setup(27,IO.IN) #sensor1split
IO.setup(23,IO.IN) #sensor5marker
#coloursensor
IO.setup(signal,IO.IN, pull_up_down=IO.PUD_UP)
IO.setup(22,IO.OUT)
IO.setup(4,IO.OUT)


# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT= 21
FORWARD_LEFT_PIN = 26
REVERSE_LEFT_PIN = 19
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 5
FORWARD_RIGHT_PIN = 13
REVERSE_RIGHT_PIN = 6



driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT,True,0,1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT,True,0,1000)
forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)
Flag = 0
Flag2 = 0
Flag3=0
marker= 0


def stop():

                forwardLeft.value = False
                reverseLeft.value = False
                forwardRight.value = False
                reverseRight.value = False
                driveLeft.value = 0
                driveRight.value = 0

                
def forward():


                forwardLeft.value = True
                reverseLeft.value = False
                forwardRight.value = True
                reverseRight.value = False
                driveLeft.value = 1
                driveRight.value = 1

def forwardSlow():


                forwardLeft.value = True
                reverseLeft.value = False
                forwardRight.value = True
                reverseRight.value = False
                driveLeft.value = 0.5
                driveRight.value = 0.5


   
def back():

                forwardLeft.value = False
                reverseLeft.value = True
                forwardRight.value = False
                reverseRight.value = True 
                driveLeft.value = 1.0
                driveRight.value = 1.0


     
def left():

                forwardLeft.value = False
                reverseLeft.value = True
                forwardRight.value = True
                reverseRight.value = False
                driveLeft.value = 0.2
                driveRight.value = 0.2

         
def right():

                forwardLeft.value = True
                reverseLeft.value = False
                forwardRight.value = False
                reverseRight.value = True
                driveLeft.value = 1.0
                driveRight.value = 1.0


try:
        while 1:

           

            if(IO.input(23) == True and IO.input(17) == False): #marker counter code 

                   time.sleep(1)
                   if(marker < 2):
                       marker = marker + 1
                       print ('%d\n' % marker) 


            if(IO.input(27) == False):

                   if(IO.input(20) == True and IO.input(12)==False and IO.input(17) == False):    #simple line follower code
                       forward()
                       if(IO.input(20) == False and IO.input(12) == False and IO.input(17)==True): #regular Error correction
                           right()
                       elif(IO.input(17)== False and IO.input(20) == False and IO.input(12) == True): #regular error correction
                           left()
               
                       elif(IO.input(20) == True and IO.input(17)==True and IO.input(12) == False):
                           left()

                       elif(IO.input(4) == False and IO.input(23) == False):
                           left() 

                     #  elif(IO.input(17)== False and IO.input(20) == True and IO.input(12) == True): #regular error correction
                      #     left()


            if(IO.input(27) == True):
                   if(marker == 1 and Flag3 == 0): 
                        left()    #90 degree code dont forget
                        Flag3 = 1
                   if(marker == 1 and Flag3 == 1):
                        forward()
                      
                   if(marker == 2 and Flag3 == 1):
                        left() #90 degree code
                        Flag3 = 0
                   if(marker == 4 and Flag3 == 0):
                        forward()
                        
                    
                   if(IO.input(20) == True and IO.input(12) == True and IO.input(17)==True and IO.input(23) == True and IO.input(4) == True):
                        forward()

                   if(IO.input(20) == True and IO.input(12) == True and IO.input(17)==True and IO.input(23) == True and IO.input(4) == False):
                        left()

                

            if(marker == 50):
                 stop()
                 time.sleep(5)


                 jackFlag = 1

                 time.sleep(10)


            if(marker == 51):
                 stop()
                 time.sleep(5)
                 if(jackFlag==1):
                     jackFlag = 0





except KeyboardInterrupt:
    IO.cleanup()




   

 


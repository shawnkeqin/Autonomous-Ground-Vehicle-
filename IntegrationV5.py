import serial
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

#sensor define except colour sensor
IO.setup(20,IO.IN) #GPIO 14 -> IR sensor as input #sensor3black
IO.setup(25,IO.IN)#switch
IO.setup(17,IO.IN) #sensor4white
IO.setup(12,IO.IN) #sensor2white
IO.setup(27,IO.IN) #sensor1split
IO.setup(23,IO.IN) #sensor5marker
IO.setup(4,IO.IN)  #sensor6FishHook


#RC define
##ser = serial.Serial('/dev/ttyACM0',9600)UNCOMENTTTTTTTTTTTTTTTTTTTTTTTT
#speed = [0,4]
#direction = [0,4]
#throttle = [0,4]
#jack = [0,4]

# Motor A, Left Side GPIO CONSTANTS
PWM_LEFT= 21
DIR_LEFT = 26
# Motor B, Right Side GPIO CONSTANTS
PWM_RIGHT = 5
DIR_RIGHT = 13

#MOTOR output GPIO define
IO.setup(PWM_LEFT,IO.OUT)
IO.setup(DIR_LEFT,IO.OUT)
IO.setup(PWM_RIGHT,IO.OUT)
IO.setup(DIR_RIGHT,IO.OUT)
#set up PWM
P_LEFT = IO.PWM(PWM_LEFT,1000)#jjjjjjjjghjjjjjjjjjjjjjjjjjjjjjjjjjjjj
P_RIGHT = IO.PWM(PWM_RIGHT,1000)
P_LEFT.start(0)
P_RIGHT.start(0)

#************************
#some variable declarations
Flag = 0
Flag2 = 0
Flag3=0
marker= 0

#************************

#mode gpio define
IO.setup(19,IO.IN)
#***************************************

def stop():

                IO.output(DIR_LEFT,IO.HIGH)
                IO.output(DIR_RIGHT,IO.LOW)
                P_LEFT.ChangeDutyCycle(0)
                P_RIGHT.ChangeDutyCycle(0)
                #forwardLeft.value = False
                #reverseLeft.value = False
                #forwardRight.value = False
                #reverseRight.value = False
                #driveLeft.value = 0
                #driveRight.value = 0

                
def forward():


                IO.output(DIR_LEFT,IO.HIGH)
                IO.output(DIR_RIGHT,IO.HIGH)
                P_LEFT.ChangeDutyCycle(80)
                P_RIGHT.ChangeDutyCycle(80)
                
                #forwardLeft.value = True
                #reverseLeft.value = False
                #forwardRight.value = True
                #reverseRight.value = False
                #driveLeft.value = 1
                #driveRight.value = 1

def forwardSlow():

                IO.output(DIR_LEFT,IO.LOW)
                IO.output(DIR_RIGHT,IO.HIGH)
                P_LEFT.ChangeDutyCycle(40)
                P_RIGHT.ChangeDutyCycle(40)
                
                
##                
##                
##                forwardLeft.value = True
##                reverseLeft.value = False
##                forwardRight.value = True
##                reverseRight.value = False
##                driveLeft.value = 0.5
##                driveRight.value = 0.5


   
def back():##############################################
                IO.output(DIR_LEFT,IO.HIGH)
                IO.output(DIR_RIGHT,IO.LOW)
                P_LEFT.ChangeDutyCycle(80)
                P_RIGHT.ChangeDutyCycle(80)


##
##                forwardLeft.value = False
##                reverseLeft.value = True
##                forwardRight.value = False
##                reverseRight.value = True 
##                driveLeft.value = 1.0
##                driveRight.value = 1.0


     
def left():
    
                IO.output(DIR_LEFT,IO.HIGH)
                IO.output(DIR_RIGHT,IO.HIGH)
                P_LEFT.ChangeDutyCycle(0)
                P_RIGHT.ChangeDutyCycle(75)

##
##
##                forwardLeft.value = False
##                reverseLeft.value = True
##                forwardRight.value = True
##                reverseRight.value = False
##                driveLeft.value = 0.2
##                driveRight.value = 0.2

         
def right():
    
                IO.output(DIR_LEFT,IO.LOW)
                IO.output(DIR_RIGHT,IO.LOW)
                P_LEFT.ChangeDutyCycle(75)
                P_RIGHT.ChangeDutyCycle(0)
   
    
##
##                forwardLeft.value = True
##                reverseLeft.value = False
##                forwardRight.value = False
##                reverseRight.value = True
##                driveLeft.value = 1.0
##                driveRight.value = 1.0




 #1 rc; 0 auto

def main():
    modeNo = 1#CHANGE THIS TO MODE ZEROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    #some variable declarations
    Flag = 0
    Flag2 = 0
    Flag3=0
    marker= 0
    a=0
    90Flag = 0
    FlagSplit = 0
    #modeNo=IO.input(19)
    #print(modeNo)
    while 1:
##        modeNo = int (ser.readline(),16) HALLLLLLLLLLLLOOOOOOOOOOOOOOOOOOO
        #print (modeNo)
        if modeNo==1: #auto
##            #reset speed
##            IO.output(DIR_LEFT,IO.HIGH)
##            IO.output(DIR_RIGHT,IO.LOW)
##            P_LEFT.ChangeDutyCycle(0)
##            P_RIGHT.ChangeDutyCycle(0)
            #reset ends
           # a=a+1
           # print(a)
            
##            forward()
            print('something')
 #           forward()
            if(IO.input(23) == True and IO.input(17) == False): #marker counter code 

                   time.sleep(1)
                   if(marker < 2):
                       marker = marker + 1
                       print ('%d\n' % marker) 
##correct
##
            if(IO.input(27) == False):

                   if(IO.input(20) == True and IO.input(12)==False and IO.input(17) == False):    #simple line follower code
                       forward()
                       print('forward')
                   if(IO.input(20) == False and IO.input(12) == False and IO.input(17)==True): #regular Error correction
                           #right()#turned right, veer left,
                       left()
                       print('left')
                   if(IO.input(17)== False and IO.input(20) == False and IO.input(12) == True): #regular error correction
                           #left()#turned left, veer right
                       right()
                       print('right')
##joint path code here:

                   if(IO.input(12)==1 and IO.input(20)==1 and IO.input(17)==1):
                       left()
                       #elif(IO.input(20) == True and IO.input(17)==True and IO.input(12) == False): WHAT IS THIS FOR TO TESST
                       #    left()#i cant make sense of why ever this would be left

                       #elif(IO.input(4) == False and IO.input(23) == False):#SPLIT PATH CODE PIECE NOT TESTED
                       #    left() 

                     #  elif(IO.input(17)== False and IO.input(20) == True and IO.input(12) == True): #regular error correction
                      #     left()
           if(IO.input(4)==1):
                        90Flag = 0
##this section onwards is the split path decision making code: this is phase 2: remove wite tape over sensor 1
            if(IO.input(27) == True):
                   if(IO.input(17) == 1 and IO.input(20) == 1):
                        FlagSplit = 1

                   if(FlagSplit == 1):
                        left()
                        if(IO.input(4) == 0):
                            FlagSplit = 0
                            90Flag = 1

                   if(IO.input(20) == 1 and IO.input(4)==0 and 90Flag == 1):
                        left()

                   if(IO.input(4)==1):
                        90Flag = 0

                   if(IO.input(4) == 1 and IO.input(23) == 1):
                        Forward()


        
                       









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


##            if(marker == 50):
##                 stop()
##                 time.sleep(5)
##
##
##                 jackFlag = 1
##
##                 time.sleep(10)
##
##
##            if(marker == 51):
##                 stop()
##                 time.sleep(5)
##                 if(jackFlag==1):
##                     jackFlag = 0
            #modeNo = IO.input(19)
            
            #print (modeNo)

##        
##            """throttle 0~100;forward 2;reverse 1;left 2 right 1; jack up 1 down 2 """
##        elif (modeNo==0): #RC
##            #print ('b')
##            
##            
##            #read RC value
##            
##            #read_serial=ser.readline()
##            #print (read_serial)
##            #speed[0] = str(int (ser.readline(),16))
##            #print (speed[0])    
##            #direction[0] = str(int (ser.readline(),16))
##            #print (direction[0])
##            #throttle[0] = str(int (ser.readline(),16))
##            #print (throttle[0])
##            #jack[0] = str(int (ser.readline(),16))
##            #print (jack[0])
##            speed = int (ser.readline(),16)
##            direction = int (ser.readline(),16)
##            throttle = int (ser.readline(),16)
##            jack = int (ser.readline(),16)
##            
##            #RC control starts : only here, the steering is neutral steering
##            if speed == 0 :
##                if direction == 0:
##                    IO.output(DIR_LEFT,IO.HIGH)
##                    IO.output(DIR_RIGHT,IO.LOW)
##                    P_LEFT.ChangeDutyCycle(0)
##                    P_RIGHT.ChangeDutyCycle(0)
##                elif direction == 1: #right
##                    IO.output(DIR_LEFT,IO.LOW)
##                    IO.output(DIR_RIGHT,IO.LOW)
##                    P_LEFT.ChangeDutyCycle(throttle)
##                    P_RIGHT.ChangeDutyCycle(throttle)
##                elif direction == 2: #left
##                    IO.output(DIR_LEFT,IO.HIGH)
##                    IO.output(DIR_RIGHT,IO.HIGH)
##                    P_LEFT.ChangeDutyCycle(throttle)
##                    P_RIGHT.ChangeDutyCycle(throttle)
##                
##            elif speed==1:
##                #reverse
##                if direction == 0:
##                    IO.output(DIR_LEFT,IO.HIGH)
##                    IO.output(DIR_RIGHT,IO.LOW)
##                    P_LEFT.ChangeDutyCycle(throttle)
##                    P_RIGHT.ChangeDutyCycle(throttle)
##                elif direction == 1: #right
##                    IO.output(DIR_LEFT,IO.HIGH)
##                    IO.output(DIR_RIGHT,IO.LOW)
##                    P_LEFT.ChangeDutyCycle(throttle)
##                    P_RIGHT.ChangeDutyCycle(0)
##                elif direction == 2: #left
##                    IO.output(DIR_LEFT,IO.HIGH)
##                    IO.output(DIR_RIGHT,IO.LOW)
##                    P_LEFT.ChangeDutyCycle(0)
##                    P_RIGHT.ChangeDutyCycle(throttle)
##            elif speed==2:
##                #forward
##                if direction == 0:
##                    IO.output(DIR_LEFT,IO.LOW)
##                    IO.output(DIR_RIGHT,IO.HIGH)
##                    P_LEFT.ChangeDutyCycle(throttle)
##                    P_RIGHT.ChangeDutyCycle(throttle)
##                elif direction == 1: #right
##                    IO.output(DIR_LEFT,IO.LOW)
##                    IO.output(DIR_RIGHT,IO.HIGH)
##                    P_LEFT.ChangeDutyCycle(throttle)
##                    P_RIGHT.ChangeDutyCycle(0)
##                elif direction == 2: #left
##                    IO.output(DIR_LEFT,IO.LOW)
##                    IO.output(DIR_RIGHT,IO.HIGH)
##                    P_LEFT.ChangeDutyCycle(0)
##                    P_RIGHT.ChangeDutyCycle(throttle)

try:
    main()
except KeyboardInterrupt:
    IO.cleanup()

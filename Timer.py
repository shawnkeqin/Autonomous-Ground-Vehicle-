import RPi.GPIO as IO
import time 
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.cleanup()
IO.setup(23,IO.IN, pull_up_down = IO.PUD_DOWN)
#IO.setup(7,IO.OUT)
#IO.output(7,0) #set ping 7 to be 0 at default
CatchTime = True
startTime = 0
startTimeRead = []
endTime = []
b = 0
a = 0
c = 0
timer = 0
timeDiff = 0
timerAt3 = 0
operator1Lag = 0
operator2Lag = 0
timerAt4 = 0
try:
        startTime = time.time()
        while True:
               timer = time.time()
               timeDiff = timer - startTime
               if(timeDiff > 9 and timeDiff<11):
                   print("home to 1")
               if(timeDiff > 19 and timeDiff<21):
                   print("1 to home")
               if(timeDiff>29 and timeDiff<31):
                   print("home to 2")
               if(timeDiff>39 and timeDiff<41):
                   print("2 to home")
               if(timeDiff>49 and timeDiff < 51):
                   print("home to 3")
                   timerAt3= time.time()
               operator1Lag = timer - timerAt3

               if(timeDiff>(59+operator1Lag) and timeDiff<(61+operator1Lag)):
                   print("3 to 1")
               if(timeDiff>(69+operator1Lag) and timeDiff<(71+operator1Lag)):
                   print("1 to home")
               if(timeDiff>(79+operator1Lag) and timeDiff<(81+operator1Lag)):
                   print("home to 4")
                   timerAt4= time.time()
               operator2Lag = timer - timerAt4
               if(timeDiff>(89+operator1Lag+operator2Lag) and timeDiff<(operator1Lag+operator2Lag+91)):
                   print("4 to 2")
               if(timeDiff>(99+operator1Lag+operator2Lag) and timeDiff<(101+operator1Lag+operator2Lag)):
                   print("2 to home")

                      
              #  print ('difference in seconds\n', c) 
               # print ('start time:',startTimeRead)
                #print ('end time:',endTime)




except KeyboardInterrupt:
    IO.cleanup()


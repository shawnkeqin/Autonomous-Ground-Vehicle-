import RPi.GPIO as GPIO
import time



s2 = 22
s3 = 4
signal = 16
NUM_CYCLES = 10


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(22,GPIO.OUT)
  GPIO.setup(4,GPIO.OUT)
  print("\n")
  




def loop():
  temp = 1
  while(1):  

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start 
    red  = NUM_CYCLES / duration
    print('red: %d\n' % red) 
   
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    print('blue: %d\n' % blue) 

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    print('green: %d\n\n\n' % green)

      
    #if green<15000 and green>10500 and red<18000 and red>13000 and blue <16500 and blue > 13000: #green-7000 blue - 7000 
     # print("red")
      #temp=1
      
   # elif red<12000 and  blue<12000 and green>12000:
    #  print("green")
     # temp=1
    #elif green<17000 and green > 14000 and red<14000 and red > 10000 and blue<17500 and blue>13500: #green - 7000 red -7000
     # print("blue")
     # temp=1
    #elif red>10000 and green>10000 and blue>10000 and temp==1:
     # print("place the object.....")
      #temp=0

  

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()

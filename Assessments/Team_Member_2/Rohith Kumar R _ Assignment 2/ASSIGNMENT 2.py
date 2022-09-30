import random
from time import *
gate=True
while(gate):
    t = random.randint(0,50)
    h = random.randint(10,50)
    if t>45 and h<40:
        print("Temperature =",t,"Humidity =",h)
        print("ALARM ON")
        gate=False
    else:
        print("Temperature =",t,"Humidity",h)
    sleep(1);
"""
OUTPUT:
Temperature = 27 Humidity 38
Temperature = 36 Humidity 39
Temperature = 23 Humidity 40
Temperature = 24 Humidity 25
Temperature = 10 Humidity 40
Temperature = 17 Humidity 30
Temperature = 17 Humidity 35
Temperature = 48 Humidity = 16
ALARM ON
"""

"""
Build a python code, (generated with random function to a variable) and 
Assume u get temperature and humidity values 
write a condition to continuously detect alarm in case of high temperature.

"""

import random
def detect(temperature,humidity):
    if(humidity<30):
        if(temperature>50):
            print("Humidity : ",humidity,"Temperature : ",temperature,
                  "HAZARDOUS!!! TURN ON ALARM")
            
for i in range(0,15):
    humidity = random.randint(15,55)
    temperature = random.randint(40,80)
    detect(temperature,humidity)
  
  

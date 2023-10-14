#!/usr/bin/python3
import math

current_temperature = 10
thereshold = 0.00001
previous_temperature = current_temperature - thereshold

def efficiency(temperature):
  -5.968 + 1.0155 * temperature - 0.0603282 * temperature ** 2 + 0.00155011 * temperature ** 3 - 1.4187 * 10 ** -5 * temperature ** 4  

previous_efficency = efficiency(previous_temperature)


while True:
     
     current_efficency = efficiency(current_temperature)
     print(current_temperature, current_efficency, previous_temperature, previous_efficency)
     
     if previous_efficency >= current_efficency:
        print(f"the optimized temperature estimate is {current_temperature}")  
        break
     
     else: 
        previous_temperature = current_temperature
        previous_efficency = current_efficency
        current_temperature += thereshold
        
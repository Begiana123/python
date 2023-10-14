#!/usr/bin/python3
import math


current_temperature = 10
thereshold = 0.00001
previous_temperature = current_temperature - thereshold
previous_efficency = -5.968 + 1.0155 * previous_temperature - 0.0603282 * previous_temperature ** 2 + 0.00155011 * previous_temperature ** 3 - 1.4187 * 10 ** -5 * previous_temperature ** 4  


while True:
     current_efficency = -5.968 + 1.0155 * current_temperature - 0.0603282 * current_temperature ** 2 + 0.00155011 * current_temperature ** 3 - 1.4187 * 10 ** -5 * current_temperature ** 4 
     print(current_temperature, current_efficency, previous_temperature, previous_efficency)
     
    

     if previous_efficency >= current_efficency:
        print(f"the optimized temperature estimate is {current_temperature}")  
        break
     
     else: 
        previous_temperature = current_temperature
        previous_efficency = current_efficency
        current_temperature += thereshold






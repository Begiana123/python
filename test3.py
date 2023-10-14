#!/usr/bin/python3

previous_temperature = 10.0
thereshold = 0.01

def efficiency(temperature):
   return -5.968 + 1.0155 * temperature - 0.0603282 * temperature ** 2 + 0.00155011 * temperature ** 3 - 1.4187 * 10 ** -5 * temperature ** 4  

next_temperature = previous_temperature + thereshold
previous_efficency = efficiency(previous_temperature)


while True:
     
     next_efficency = efficiency(next_temperature)
     print(f"{previous_temperature:.2f}", previous_efficency, f"{next_temperature:.2f}", next_efficency)
     
     if next_efficency <= previous_efficency:
        print(f"the optimized temperature estimate is {previous_temperature:.2f}")  
        break
     
     else: 
        previous_temperature = next_temperature
        previous_efficency = next_efficency
        next_temperature +=thereshold

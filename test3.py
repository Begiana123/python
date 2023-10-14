#!/usr/bin/python3

previous_temperature = float(45)
thereshold = 0.000001


def efficiency(temperature):
    return -5.968 + 1.0155 * temperature - 0.0603282 * temperature ** 2 + 0.00155011 * temperature ** 3 - 1.4187 * 10 ** -5 * temperature ** 4


def derivative(temperature):
    return 1.0155 - 0.0603282 * 2 * temperature ** 1 + 0.00155011 * 3 * temperature ** 2 - 1.4187 * 10 ** -5 * 4 * temperature ** 3


def to_string(temperature):
    return f"{temperature:.6f}"


next_temperature = previous_temperature + derivative(previous_temperature)
previous_efficency = efficiency(previous_temperature)


while True:

    next_efficency = efficiency(next_temperature)

    # print(to_string(previous_temperature), f"{previous_efficency:.6f}", to_string(next_temperature), f"{next_efficency:.6f}")

    if abs(next_efficency - previous_efficency) < thereshold:
        print("The optimized temperature estimate is",
              to_string(previous_temperature))
        break

    else:
        previous_temperature = next_temperature
        previous_efficency = next_efficency
        next_temperature = previous_temperature + \
            derivative(previous_temperature)

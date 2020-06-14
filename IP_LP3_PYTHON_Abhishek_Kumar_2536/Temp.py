# Write a Python program to convert temperatures to and
# from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in
# celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius


def convert_temp(temperature, unit):
    """
    :param temperature: integer value of temperature
    :param unit: provide current units, C or F, will convert to other
    :return:
    """
    result = 0
    if unit.upper() == "C":
        result = temperature * (9/5) + 32
    elif unit.upper() == "F":
        result = (temperature - 32) * (5/9)
    return int(result)


print(convert_temp(45, "F"))

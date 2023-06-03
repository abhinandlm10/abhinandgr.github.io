
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
 
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
 
temperature = float(input("Enter a temperature value: "))
scale = input("Enter the temperature scale (Celsius or Fahrenheit): ")
 
if scale.lower() == "celsius":
    converted_temp = celsius_to_fahrenheit(temperature)
    print(f"The equivalent temperature in Fahrenheit is: {converted_temp:.2f} °F")
elif scale.lower() == "fahrenheit":
    converted_temp = fahrenheit_to_celsius(temperature)
    print(f"The equivalent temperature in Celsius is: {converted_temp:.2f} °C")
else:
    print("Invalid temperature scale. Please enter Celsius or Fahrenheit.")
 
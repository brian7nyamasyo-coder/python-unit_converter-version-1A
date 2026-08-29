#UNIT CONVERTER
print("****UNIT CONVERTER****")

#Kilometres to miles
kilometres = float(input("\nEnter the kilometres: "))
miles = kilometres * 0.621371

print(f"{kilometres} km = {miles:.2f} miles")
input("Press Enter to continue")

#Celcius to Fahrenheit
celcius = float(input("\nEnter the degrees: "))
fahrenheit = (celcius * 9/5) + 32

print(f"{celcius}℃ = {fahrenheit:.2f}℉")
input("Press Enter to continue")

#Kilogram to Pounds
kilogram = float(input("\nEnter the kilogram: "))
pounds = kilogram * 2.20462

print(f"{kilogram} kg = {pounds:.2f} pounds")
input("Press Enter to continue")

#Centimeters to feet
centimeters = float(input("\nEnter height/length in centimeters: "))
feet = centimeters / 30.48

print(f"{centimeters} cm = {feet:.2f} feet")
print("####😊THANK YOU FOR USING OUR UNIT CONVERTER####")



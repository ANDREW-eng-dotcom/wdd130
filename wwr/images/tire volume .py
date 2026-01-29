import math
import datetime

#prompt the user for input 
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#calculate the volume
tire_volume = (math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter)) / 40000000

#print approximate volume into two decimals 
print("The approximate volume is {:.2f} litres".format(tire_volume))

#get current date 
current_date = datetime.date.today()

#open file for appending
with open('volume.txt', 'a') as f:
    #write data to the file.
    f.write('{},{},{},{},{}\n'.format(current_date, tire_width, aspect_ratio, wheel_diameter, round(tire_volume, 2)))
    


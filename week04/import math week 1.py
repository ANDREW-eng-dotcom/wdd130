import math
from datetime import datetime

def main():
    #1.prompt for three numbers
    width =float(input("enter the width of the tire in mm(ex 205):"))
    aspect_ratio = float (input("Enter the aspect ratio of the tire(ex 60):"))
    diameter = float (input ("Enter the diameter of the wheel in inches"))
    
    #2.Calculate the correct tire volume in liters
    # Formula:v=(pi*w^2*a*(W*a+2540*d))/10000000000
    volume= math.pi * width**2*aspect_ratio*(width*aspect_ratio + 2540*diameter)/10000000000
    
    #3.Print the volume with 2 digits after the decimal point
    print (f"The approximate volume is {volume:.2f} liters.")
    
    #4.Get the current datetime
    current_date = datetime.now()
    
    #5.Open volumes.txt in append mode ('a') so existing data is not erased
    with open ("volumes.txt","a") as volume_file:
        # 6.Print width,aspect ratio,diameter,and volume to the file
        # Format: date,width,aspect_ratio,diameter,volume
        print(f"{current_date:%Y-%m-%d},{width:.0f},{aspect_ratio:.0f},{diameter:.0f},{volume:.2f}",file=volume_file)
     
    if __name__ == "_main_":
        main()    



#GP106 Group Project
#Group 39
#Treadmill Dashboard

# To run program with default parameters
# python E18_G_039.py

import argparse
import math

# Define your functions here
#difining the functions
''' A set of functions for a treadmill dashboard outputs'''
# time in minutes
# weight in kg
# height in cm
# motor_rate in RPM
# rdius in cm

def speed(motor_rate,radius):
    '''
    A function to calculate the running,walking speed
    in the tredmill
    Example:
    >>> speed(300,12)
    3.7699111843077517
    >>> speed(400,12)
    5.026548245743669
        
    '''
    speed =( motor_rate * math.pi*2*radius)/(60*100)
    # return speed in m/s
    return speed

def distance(time,motor_rate,radius):
    ''' A function to calculeted the virtual distance walked,ran
    Example:
    >>> distance(30,300,12)
    6785.840131753953
    >>> distance(25,400,12)
    7539.822368615503
    '''
    
    distance = speed(motor_rate,radius) *time*60
    # retirn distance in m
    return distance



def calories(weight,height,motor_rate,radius,time):
    '''
    A function to calculate the calories burnt from begening
    Example:
    >>> calories(64,154,300,12,30)
    467.89376843225307
    >>> calories(76,162,300,12,25)
    463.01987501108374
    '''
    if speed(motor_rate,radius) <= 1.65405:
      oxygen = (0.1*speed(motor_rate,radius)*60)+ 3.5     # oxygen per minute when walking
    else:
       oxygen = (0.2*speed(motor_rate,radius)*60)+ 3.5    # oxygen per minute when running
    # calories per minute
    cal = (oxygen * weight)/200

    calories = cal * time

    return calories 

def steps(time,motor_rate,radius,height):
    '''
    A function to calculate the no.of steps ran,walked
    Example:
    >>> steps(25,300,12,164)
    16697.769965338768
    '''
    
    do = distance(time,motor_rate,radius)    

    # calculating average stride lenth in m per stride
    stride = ((height/2.54)*0.413* 2.54)/100

    # calculating no of steps
    steps = do / (stride/2)
    return steps


# Don't change the the code below this point
if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--motor", type=int, dest="motor_rate", help="EXAMPLE: 3", default=3)
    args.add_argument("--radius", type=str, dest="radius", help="EXAMPLE: 8 cm", default="8 cm")
    args.add_argument("--weight", type=str, dest="weight", help="EXAMPLE: 50 kg", default="50 kg")
    args.add_argument("--height", type=str, dest="height", help="EXAMPLE: 63 in", default="63 in")
    args.add_argument("--time", type=str, dest="time", help="EXAMPLE: 1 h", default="1 h")
    
    args=args.parse_args()

# Don't change the the code above this point

    


# indentifying and unit convertion

# height
u_hl = args.height.split(" ")
if u_hl[1]=="cm":
  args.height = float(u_hl[0])
elif u_hl[1]=="m":
  args.height = float(u_hl[0]) * 100
elif u_hl[1]=="in":
  args.height = float(u_hl[0]) * 2.54
elif u_hl[1]=="ft":
  args.height = float(u_hl[0]) * 30.48
else:
  print("invalid input")



# weight
u_wl = args.weight.split(" ") 
if u_wl[1]=="kg":
  args.weight = float(u_wl[0])
elif u_wl[1]=="g":
  args.weight = float(u_wl[0]) /1000
elif u_wl[1]=="lb":
  args.weight = float(u_wl[0]) * 0.453592
else:  
  print("invalid input")
                


# radius
u_rl = args.radius.split(" ") 
if u_rl[1]=="mm":
  args.radius = float(u_rl[0])/10
elif u_rl[1]=="cm":
  args.radius = float(u_rl[0])
elif u_rl[1]=="m":
  args.radius = float(u_rl[0]) * 100
else:  
  print("invalid input")


# time
u_tl = args.time.split(" ") 
if u_tl[1]=="s":
  args.time = float(u_tl[0])/60
elif u_tl[1]=="min":
  args.time = float(u_tl[0])
elif u_tl[1]=="h":
  args.time = float(u_tl[0]) * 60
else:  
  print("invalid input")


# motor_rate
#No units for motor_rate
u_m1 = args.motor_rate
  
        



#Outputs

#calculating and displaying current speed
sp = speed(args.motor_rate,args.radius)
print (int(sp),"m/s")
      
#calculating and diplaying total distance
dis = distance(args.time,args.motor_rate,args.radius)
print (int(dis),"m")
    
#calculating and displaying total calories burnt
calo = calories(args.weight,args.height,args.motor_rate,args.radius,args.time)
print (int(calo),"cal")
    
#calculating and displaying the no. of steps
stp = steps(args.time,args.motor_rate,args.radius,args.height)
print(int(stp))

    

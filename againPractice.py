# first install the module  in this video we will use the module is this 

from pytube import *

# first enter the link of video 
# we use input function for  this 

link = input("Enter The vedio link : ")


# after link we need into you tube function for other working and store the address into some vaiable 


vD = YouTube(link)# Y and T must be larger 

# after this we need to get the quality of video 

vdL = vD.streams.all()

# after this we need to print to screen 

vdlP = list(enumerate(vdL))

for i in vdlP:
    print(i)
   

# after this we need to get the input from user which quality you want to download 

vdI = int(input('Enter the input : '))

# after select the input we need to pass into  quality jadir sa hum na quality le thi

vdL[vdI].download()

print ("your downloading is complete ")
    
    

import os
from datetime import datetime
import time



def main():

    #Call the function to start for the text LEDs
    os.system("sudo ~/display16x32/rpi-rgb-led-matrix/text-example -f ~/display16x32/rpi-rgb-led-matrix/fonts/5x8.bdf")
    
    #Now display the time every .2 seconds
    for I in range(0,9):
        my_time = datetime.now().strftime("%A %b,%d %I:%M") 
        time.sleep(10)  
        os.system("%s" %my_time)

    

main()



#sudo ./text-example -f fonts/5x8.bdf -r 16 -c2 -y8 -C255,0,0
# We want to change his code, Idk if we should add a CNTRL+D To exit out?

import os
from datetime import datetime
import time
import pyowm
import re

def weather():
    echo = "echo"
    owm = pyowm.OWM('98adaec88275ac5e03a288efaee18a11')
    #Today's Weather
    observation = owm.weather_at_place('Chicago,il')
    w = observation.get_weather()

    #Tomorrow's Weather
    #Not implemented yet ^^""


    Intro_today= "For today's weather in Chicago"
    status_today = "Looks like we have a "+ w.get_status()

    clouds = str(w.get_clouds())
    clouds_today = "There's " + clouds + "% clouds in the sky"

    x= str(w.get_temperature('fahrenheit'))

    x = re.sub("[{},:']",'',x)
    x= re.sub("[t]",'T',x)
    x = re.sub("Temp_kf None",'',x)
    temp_today = x

    Npp= (len())

    for x in range (Npp):
        os.system( echo + " " + Intro_today)
        time.sleep(.1)
    for x in range (Npp):
        os.system( echo + " " + status_today)
        time.sleep(.1)
    for x in range (Npp):
        os.system( echo + " " + clouds_today)
        time.sleep(.1)
    for x in range (Npp):
        os.system( echo + " " + temp_today)
        time.sleep(.1)




def main():
    echo = "echo"

    #Call the function to start for the text LEDs
   # os.system("sudo ~/display16x32/rpi-rgb-led-matrix/text-example -f ~/display16x32/rpi-rgb-led-matrix/fonts/5x8.bdf")

    #Now display the time every .2 seconds
    startup = 0;
    Intro = "Good Freaking Morning Richie and Roger"

    while True:
        Npp = (len(Intro)*10)

	#if startup == 0:
        for y in range (Npp):
            time.sleep(.1)
            os.system(echo + " " + Intro)
        startup = 1
        my_time = datetime.now().strftime("%A %b,%d %I:%M%p")
        Npp = (len(my_time)* 10)

        for x in range (Npp):
            my_time = datetime.now().strftime("%A %b,%d %I:%M%p")
            time.sleep(.1)
            os.system(echo + " " + my_time)
        weather()
main()



#sudo ./text-example -f fonts/5x8.bdf -r 16 -c2 -y8 -C255,0,0


import os
from datetime import datetime
import time
import pyowm
import re
import json
from googlefinance import getQuotes

def weather():
    echo = "echo"
    owm = pyowm.OWM('98adaec88275ac5e03a288efaee18a11')
    #Today's Weather
    observation = owm.weather_at_place('Chicago,il')
    w = observation.get_weather()

    #Tomorrow's Weather
    #Not implemented yet ^^""


    Intro_today= "For todays weather in Chicago"
    status_today = "Looks like we have a "+ w.get_status()

    clouds = str(w.get_clouds())
    clouds_today = "Theres " + clouds + "% clouds in the sky"

    x= str(w.get_temperature('fahrenheit'))

    x = re.sub("[{},:']",'',x)
    x= re.sub("[t]",'T',x)
    x = re.sub("Temp_kf None",'',x)
    temp_today = x

    Npp= (len(Intro_today))

    for x in range (Npp):
        os.system( echo + " " + Intro_today)
        time.sleep(.1)

    Npp= (len(status_today))
    for x in range (Npp):
        os.system( echo + " " + status_today)
        time.sleep(.1)

    Npp= (len(clouds_today))
    for x in range (Npp):
        os.system( echo + " " + clouds_today)
        time.sleep(.1)

    Npp= (len(temp_today))
    for x in range (Npp):
        os.system( echo + " " + temp_today)
        time.sleep(.1)

def twitter():

    tweets_data_path = 'twitter_data.txt'
    tweets_data = []
    tweets_file = open(tweets_data_path, 'r')
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    for tweeter in tweets_data:
        Npp = (len(tweeter['text'])*10)
        for y in range (Npp):
            time.sleep(.1)
            os.system(echo + " " + tweeter['text'])
def stocks():
    echo = "echo"
    stock = json.load(getQuotes('AAPL'), indent = 2)
    stockPrice = stock["LastTradePrice"]
    print stock
    print stock["LastTradePrice"]           
#    while True:
#        Npp = (len(stock)*10)
#	for y in range (Npp):
#	    time.sleep(.1)
#	    os.system(echo + "" + stock) 

def main():
    echo = "echo"
   # stocks()
    #Call the function to start for the text LEDs
   # os.system("sudo ~/display16x32/rpi-rgb-led-matrix/text-example -f ~/display16x32/rpi-rgb-led-matrix/fonts/5x8.bdf")

    #Now display the time every .2 seconds
    startup = 0;
    Intro = "Richies desk"
    myMessage = input('Enter Custom Message: ')

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

	for timer in range(0,10):
	    timerStr = str(timer)
	    os.system(echo + " " + timerStr)
	    time.sleep(1)
	    Npp = (len(myMessage)* 10)
	for z in range (Npp):
	    time.sleep(.1)
	    os.system(echo + " " + myMessage)
        #weather()
        #twitter()
#	while True:
#	    my_time = datetime.now().strftime("%I:%M:%S")
#	    message= "Go Cubs Go! Go Cubs Go! Hey Chicago What do you say? Cubs are gonna win today!"
#	    Npp = (len(message)*10)
#	    for x in range (Npp):
#	        os.system(echo + " " +  message)
#	        time.sleep(.1)
main()



#sudo ./text-example -f fonts/5x8.bdf -r 16 -c2 -y8 -C255,0,0


import urllib2
import simplejson
import twitter
import json
import time
import datetime


api = twitter.Api(consumer_key='*******************',
            consumer_secret='*********************',
             access_token_key='***********************', 
             access_token_secret='**********************')



referral_url = "http://bit.ly/GSSmmg"

url = "http://api.wunderground.com/api/********************/conditions/q/VA/Blacksburg.json"
#current_weather = ""

#now = datetime.datetime.now()

#api.PostUpdate("Starting Service") //don't uncomment

last_update = api.GetUserTimeline(1947828650)[0].text
print last_update
def mainScript():
       
    last_update = api.GetUserTimeline('bleaksburg')[0].text
    
    #timenow = now.strftime("%I:%M:%S")
    response = urllib2.urlopen(url).read()
    data = json.loads(response) #print data
    temp = str(data['current_observation']['temp_f']) #temp in degrees F
    wind  = str(data['current_observation']['wind_string']) #wind_string from json
    humid = str(data['current_observation']['relative_humidity']) #humidity
    weather  = str(data['current_observation']['weather']) #what it looks like in the sky

    if(wind == "Calm"):
        wind_change = "The wind is"
    else:
        wind_change = "The wind is blowing"
    #The Time is %s. timenow
    current_weather = "It is %s. %s %s. Temperature is %s F. Humidity is %s. %s " % (weather, wind_change, wind, temp, humid, referral_url)
    if(current_weather == last_update):
        "Tweet same as last time"
    elif (current_weather != last_update):
        api.PostUpdate(current_weather)
        print current_weather
    time.sleep(300)

if __name__ = "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)




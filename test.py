import pyttsx
from datetime import datetime

time = str(datetime.now())
time2 = str('2016-10-02 06:10')
time3 = str('2016-10-02 06:12')

engine = pyttsx.init()
engine.setProperty('rate', 75)

while 1:
	if time[:16] == time2:
		voices = engine.getProperty('voices')
		for voice in voices:
    			print "Using voice:", repr(voice)
   			engine.setProperty('voice', voice.id)
    			engine.say("Hi there, how are you?")
    			engine.say("Good Morning sir! Time to wake up.")
			engine.runAndWait()
	else:
			time = str(datetime.now())


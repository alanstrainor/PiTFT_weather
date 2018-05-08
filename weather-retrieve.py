#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, syslog
import datetime
#import pygame
import signal
import time
import string
import thread
from time import sleep
from threading import Thread
from libavg import avg, gesture, app, ImageNode, player
from weather import Weather, Unit

# global vars
is_run = True
# define timer to run app every 60 seconds
starttime=time.time()
# weather icons path
iconsPath = "./icons/"
# location for Lille, FR on weather.com
weatherDotComLocationCode = 'EIXX0014'
# font colours
colourWhite = (255, 255, 255)
colourBlack = (0, 0, 0)

# update interval
updateRate = 600 # seconds
# Yahoo Weather
weather = Weather(unit=Unit.CELSIUS)
#Counter for forecast
forecastCounter = 0
# define arrays
forecastText = {}
forecastDays = {}
forecastHighs = {}
forecastLows = {}
# define global vars
station = ''
forecasts = ''
today = ''
windspeed = ''
windDir = ''
currTemp = ''
currPress = ''
imageCode = ''



player = avg.Player.get()
canvas = player.createMainCanvas(size=(480,320))
rootNode = canvas.getRootNode()
#player.setFramerate(6000)
class Weather(app.MainDiv):
	def onInit(self, parent=None):
		stationNode = avg.WordsNode(pos=(10,10), font="arial",text="Currently: " + station, parent=player.getRootNode())
		windSpeedNode = avg.WordsNode(pos=(10,30), font="arial",text="Wind Speed: " + windSpeed, parent=player.getRootNode())
		currTempNode = avg.WordsNode(pos=(10,50), font="arial",text="Temp: " + currTemp, parent=player.getRootNode())
		winDirNode = avg.WordsNode(pos=(10,70), font="arial",text="Wind Direction: " + windDir, parent=player.getRootNode())
		todayNode = avg.WordsNode(pos=(180,70), font="arial",text=today, parent=player.getRootNode())
		imgNode = avg.ImageNode(href="images/" + imageCode + ".png", pos=(10,70),parent=player.getRootNode())
		print(today + "In Weather Class")
		# Forecast for coming days
		column = 10
		for i in range(2,6):
			forecastDaysNode = avg.WordsNode(pos=(column,200), font="arial",text=forecastDays[i], parent=player.getRootNode())
			forecastTextNode = avg.WordsNode(pos=(column,220), font="arial",text=forecastText[i], parent=player.getRootNode())
			forecastHighsNode = avg.WordsNode(pos=(column,240), font="arial",text=forecastHighs[i] + "c", parent=player.getRootNode())
			forecastLowsNode = avg.WordsNode(pos=(column,260), font="arial",text=forecastLows[i] + "c", parent=player.getRootNode())
			column += 120


		#time.sleep(5)
		#retrieval()
		#player.play()
		return
	def onFrame(self):
		#print("Hello")
		pass
		#retrieval()


		pass
	def onExit(self):
		pass



def retrieval():
    # retrieve data from weather.com
    #TODO catch error and retry
    #weather = pywapi.get_weather_from_weather_com(weatherDotComLocationCode,units = 'metric')
	location = weather.lookup_by_location('dublin')
	condition = location.condition
	#print(location.atmosphere)
	now = datetime.datetime.now()
	# Get weather forecasts for the upcoming days.
	global station
	global forecasts
	global today
	global windSpeed
	global windDir
	global currTemp
	global currPress
	global imageCode

	forecasts = location.forecast
	station = location.condition.text
	today = str(now)
	windSpeed = location.wind.speed
	windDir = location.wind.direction
	currTemp = location.condition.temp
	currPress = location.atmosphere['pressure']
	imageCode = location.condition.code

	forecastCounter = 0
	forecasts = location.forecast
	for forecast in forecasts:
		forecastCounter += 1
		forecastText[forecastCounter] = forecast.text[:14]
		forecastDays[forecastCounter] = forecast.day
		forecastHighs[forecastCounter] = forecast.high
		forecastLows[forecastCounter] = forecast.low
	print(forecastText)
	print(today)


retrieval()
app.App().run(Weather())
print("after Play")



#while True:
#	app.App().run(Weather())
#	time.sleep(60.0 - ((time.time() - starttime) % 60.0))

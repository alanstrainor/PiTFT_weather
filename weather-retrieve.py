#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, syslog
import datetime
#import pygame
import signal
import time
import string
from libavg import avg, gesture, app, ImageNode, player
from weather import Weather, Unit

# global vars
is_run = True
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

now = datetime.datetime.now()

class Weather():
	def __init__(self, parent=None):
		player = avg.Player.get()
		canvas = player.createMainCanvas(size=(480,320))
		rootNode = canvas.getRootNode()
		avg.WordsNode(pos=(10,10), font="arial",text="Currently: " + station, parent=rootNode)
		avg.WordsNode(pos=(10,30), font="arial",text="Wind Speed: " + windSpeed, parent=rootNode)
		avg.WordsNode(pos=(10,50), font="arial",text="Temp: " + currTemp, parent=rootNode)
		avg.WordsNode(pos=(10,70), font="arial",text="Wind Direction: " + windDir, parent=rootNode)
		imgNode = avg.ImageNode(href="images/" + imageCode + ".png", pos=(10,70),parent=player.getRootNode())

		# Forecast for coming days
		column = 10
		for i in range(2,6):
			avg.WordsNode(pos=(column,200), font="arial",text=forecastDays[i], parent=rootNode)
			avg.WordsNode(pos=(column,220), font="arial",text=forecastText[i], parent=rootNode)
			avg.WordsNode(pos=(column,240), font="arial",text=forecastHighs[i] + "c", parent=rootNode)
			avg.WordsNode(pos=(column,260), font="arial",text=forecastLows[i] + "c", parent=rootNode)
			column += 130
		player.play()



while(is_run):
    # retrieve data from weather.com
    #TODO catch error and retry
    #weather = pywapi.get_weather_from_weather_com(weatherDotComLocationCode,units = 'metric')
	location = weather.lookup_by_location('dublin')
	condition = location.condition
	#print(location.atmosphere)

	# Get weather forecasts for the upcoming days.

	forecasts = location.forecast
	station = location.condition.text
	today = str(now)
	windSpeed = location.wind.speed
	windDir = location.wind.direction
	currTemp = location.condition.temp
	currPress = location.atmosphere['pressure']
	imageCode = location.condition.code

	forecasts = location.forecast
	for forecast in forecasts:
	#for i in range(5):
		forecastCounter += 1
		forecastText[forecastCounter] = forecast.text
		forecastDays[forecastCounter] = forecast.day
		forecastHighs[forecastCounter] = forecast.high
		forecastLows[forecastCounter] = forecast.low
	print(forecastText)
	# extract current data for today
    #today = weather['forecasts'][0]['day_of_week'][0:3] + " " \
    #      + weather['forecasts'][0]['date'][4:] + " " \
    #      + weather['forecasts'][0]['date'][:3]
    #windSpeed = int(weather['current_conditions']['wind']['speed'])
    #currWind = "{:.0f} km/h ".format(windSpeed) \
    #           + weather['current_conditions']['wind']['text']
    #currTemp = weather['current_conditions']['temperature'] \
    #           + " "+ u'\N{DEGREE SIGN}' + "C"
    #currPress = weather['current_conditions']['barometer']['reading'][:-3] \
    #            + " h
    #uv = "UV {}".format(weather['current_conditions']['uv']['text'])
    #humid = "Hum {} %".format(weather['current_conditions']['humidity'])
    # extract forecast data
    #forecastDays = {}
    #forecaseHighs = {}
    #forecaseLows = {}
    #forecastPrecips = {}
    #forecastWinds = {}
    #start = 0
    #try:
	#        test = float(weather['forecasts'][0]['day']['wind']['speed'])
    #except ValueError:
    #    start = 1
    #for i in range(start, 5):
    #    if not(weather['forecasts'][i]):
    #        break
    #    forecastDays[i] = weather['forecasts'][i]['day_of_week'][0:3]
    #    forecaseHighs[i] = weather['forecasts'][i]['high'] + u'\N{DEGREE SIGN}' + "C"
    #    forecaseLows[i] = weather['forecasts'][i]['low'] + u'\N{DEGREE SIGN}' + "C"
    #    forecastPrecips[i] = weather['forecasts'][i]['day']['chance_precip'] + "% (pluie)"
    #    forecastWinds[i] = "{:.0f}".format(int(weather['forecasts'][i]['day']['wind']['speed'])) + \
    #                       " km/h "+weather['forecasts'][i]['day']['wind']['text']
    # blank the screen
	is_run = False


app.App().run(Weather())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, syslog
import pygame
import signal
import time
import pywapi
import string
from libavg import avg, gesture, app, ImageNode, player

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


class Weather():
	def __init__(self, parent=None):
		player = avg.Player.get()
		canvas = player.createMainCanvas(size=(480,320))
		rootNode = canvas.getRootNode()
		player.play()

while(is_run):
    # retrieve data from weather.com
    #TODO catch error and retry
    weather = pywapi.get_weather_from_weather_com(weatherDotComLocationCode,units = 'metric')
    # extract current data for today
    station = weather['current_conditions']['station']
    today = weather['forecasts'][0]['day_of_week'][0:3] + " " \
          + weather['forecasts'][0]['date'][4:] + " " \
          + weather['forecasts'][0]['date'][:3]
    windSpeed = int(weather['current_conditions']['wind']['speed'])
    currWind = "{:.0f} km/h ".format(windSpeed) \
               + weather['current_conditions']['wind']['text']
    currTemp = weather['current_conditions']['temperature'] \
               + " "+ u'\N{DEGREE SIGN}' + "C"
    currPress = weather['current_conditions']['barometer']['reading'][:-3] \
                + " hPa"
    uv = "UV {}".format(weather['current_conditions']['uv']['text'])
    humid = "Hum {} %".format(weather['current_conditions']['humidity'])
    # extract forecast data
    forecastDays = {}
    forecaseHighs = {}
    forecaseLows = {}
    forecastPrecips = {}
    forecastWinds = {}
    start = 0
    try:
        test = float(weather['forecasts'][0]['day']['wind']['speed'])
    except ValueError:
        start = 1
    for i in range(start, 5):
        if not(weather['forecasts'][i]):
            break
        forecastDays[i] = weather['forecasts'][i]['day_of_week'][0:3]
        forecaseHighs[i] = weather['forecasts'][i]['high'] + u'\N{DEGREE SIGN}' + "C"
        forecaseLows[i] = weather['forecasts'][i]['low'] + u'\N{DEGREE SIGN}' + "C"
        forecastPrecips[i] = weather['forecasts'][i]['day']['chance_precip'] + "% (pluie)"
        forecastWinds[i] = "{:.0f}".format(int(weather['forecasts'][i]['day']['wind']['speed'])) + \
                           " km/h "+weather['forecasts'][i]['day']['wind']['text']
    # blank the screen



app.App().run(Weather())

from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)

# Lookup WOEID via http://weather.yahoo.com.

lookup = weather.lookup(560743)
condition = lookup.condition
#print(condition.text)

# Lookup via location name.

location = weather.lookup_by_location('dublin')
condition = location.condition
# print windspeed
print(location.wind.speed)
print(location.condition.temp)
print(location.atmosphere['humidity'])
print(location.condition.code + ' Weather code')
#print(location.date)
#print(location.item.title)
# Get weather forecasts for the upcoming days.

forecasts = location.forecast
print(location.forecast)
for forecast in forecasts:
    print(forecast.text)
    print(forecast.day)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)



# Lookup via latitude and longitude

w = Weather(Unit.CELSIUS)
lookup = w.lookup_by_latlng(53.3494,-6.2601)
condition = lookup.condition
print(condition.text)

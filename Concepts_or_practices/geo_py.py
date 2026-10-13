from  geopy.geocoders import Nominatim

geo = Nominatim(user_agent="My_App")
print(geo.geocode("ISBM pune"))


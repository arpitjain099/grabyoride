
import codecs
fi=codecs.open("output.txt","r",encoding='utf-8')
f=fi.read()
fi.close()
f=f.split("\n")
fi=codecs.open("output_geocode.txt","a+",encoding='utf-8')
from geopy.geocoders import Nominatim
for i in f:
	print i
	geolocator = Nominatim()
	location = geolocator.geocode(i)
	print((location.latitude, location.longitude))


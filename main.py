from meteoApi import Meteo
meteo = Meteo('','Catania','http://api.openweathermap.org/data/2.5/weather?q=Catania&appid=72e31309c9036feda3c461dec95b012f&lang=it&units=metric')
meteo.printMeteo()
meteo.printJson()
import urllib.request
import json
import datetime
class Meteo:
    umidita= None
    pressione= None
    temperatura= None
    alba=None
    tramonto=None
    apiKey=None
    city=None
    description=None

    def __init__(self, apiKey,city,url):
        self.city = city
        self.apiKey = apiKey
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        theResponse = json.loads(response.read())
        self.temperatura = theResponse.get('main').get('temp')
        self.pressione = theResponse.get('main').get('pressure')
        self.umidita = theResponse.get('main').get('humidity')
        self.alba= theResponse.get('sys').get('sunrise')
        self.tramonto=theResponse.get('sys').get('sunset')
        self.description= theResponse.get('weather')[0].get('description')
        
    def printMeteo(self):
        print("La mia città è :"+ self.city)
        print("La temperatura: "+str(self.temperatura))
        print("L'umidità: "+str(self.umidita)+"%")
        print("La pressione atmosferica: "+str(self.pressione))
        print("Il bollettino meteo è: "+self.description)
    def printJson(self):
        obj =  {}
        obj['temperatura'] = self.temperatura
        obj['pressione']= self.pressione
        obj['umidita']= self.umidita
        obj['alba']= datetime.datetime.fromtimestamp(self.alba).strftime('%d-%m-%Y %H:%M:%S')
        obj['tramonto']= datetime.datetime.fromtimestamp(self.tramonto).strftime('%d-%m-%Y %H:%M:%S')
        obj['description']= self.description
        obj['city'] = self.city
        return print(json.dumps(obj,indent=4, sort_keys=True))



from yapsy.IPlugin import IPlugin
import pywapi


class Weather(IPlugin):
    pi = ""
    conf = {}

    def start(self, param):
        self.pi = param.pi
        self.conf = param.conf
        for m in param.dmParsed:
          if str(m['sender_id']) == str(param.conf['user_id']):
            ms = m['text'].split()
            if (ms[0].lower() == "weather"):
                self.pi.deleteDirectMessage(m['id_str'])
                self.getWeather()


    def getWeather(self):
        code = self.conf['city_id']
        city_name = self.conf['city_name']
        weather_com_result = pywapi.get_weather_from_weather_com(code)
        #yahoo_result = pywapi.get_weather_from_yahoo(code)     
        #print("It is "
        #      + weather_com_result['current_conditions']['text'].lower() +
        #      " and " + weather_com_result['current_conditions']['temperature']
        #      + "C in " + city_name)
        self.pi.sendDirectMessage("It is "
              + weather_com_result['current_conditions']['text'].lower() +
              " and " + weather_com_result['current_conditions']['temperature']
              + "C in " + city_name)
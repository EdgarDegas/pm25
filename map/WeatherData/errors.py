class WeatherDataError(Exception): pass

class WeatherDataNetworkError(WeatherDataError): 
    """
    Network errors occoured during weather request.
    Check server network connection by visiting weather.com.cn.
    """
    pass


class CityCodeNotFound(WeatherDataError): 
    """
    Empty response message is returned,
    which indicates that no code for this city is available.
    """
    pass

class NoWeatherForCode(WeatherDataError): pass

class AQINotAvailable(WeatherDataError): pass
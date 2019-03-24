from datetime import date
from .forecast_type import ForecastType


class Forecast:
    """
    The class constructor for the Forecast class. It represents the weather
    forecast data that the parser returns. It has property definitions for
    all the data to be parsed.
    """

    def __init__(self,
                 current_temp,
                 humidity,
                 wind,
                 high_temp=None,
                 low_temp=None,
                 description='',
                 forecast_date=None,
                 forecast_type=ForecastType.TODAY):
        self._current_temp = current_temp
        self._humidity = humidity
        self._wind = wind
        self._high_temp = high_temp
        self._low_temp = low_temp
        self._description = description
        self._forecast_type = forecast_type
        if forecast_date is None:
            self.forecast_date = date.today()
        else:
            self._forecast_date = forecast_date

    @property
    def forecast_date(self):
        """
        The getter method for the forecast date. If the forecast date is not supplied, it
        will be set to the current date.
        :return: The weather forecast date.
        """
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, forecast_date):
        """
        The setter method for the forecast date. Every time we need to set the date in an instance of
        Forecast every, we need to make sure that it will be formatted accordingly.
        :param forecast_date:
        :return:
        """
        self._forecast_date = forecast_date.strftime("%a %b %d")

    @property
    def current_temp(self):
        """
        The getter method for the current weather temperature. It represents the
        current temperature. Only available when getting today's weather forecast.
        :return: The current day's temperature.
        """
        return self._current_temp

    @property
    def humidity(self):
        """
        The getter method for the day's humidity percentage for the day.
        :return: The humidity percentage.
        """
        return self._humidity

    @property
    def wind(self):
        """
        The getter method for the day's current wind levels.
        :return: The current wind levels
        """
        return self._wind

    @property
    def description(self):
        """
        The getter method for the description of the weather conditions, e.g.: Partly Cloudy
        :return: The weather conditions' description
        """
        return self._description

    def __str__(self):
        """
        An override the __str__ method to allow us to format the output when
        using print, format, and str functions.
        :return: The formatted output
        """
        temperature = None
        offset = ' ' * 4
        if self._forecast_type == ForecastType.TODAY:
            temperature = (f'{offset}{self._current_temp}\xb0\n'
                           f'{offset}High {self._high_temp}\xb0 / '
                           f'Low {self._low_temp}\xb0 ')
        else:
            temperature = (f'{offset}High {self._high_temp}\xb0 / '
                           f'Low {self._low_temp}\xb0 ')
        return (f'>> {self.forecast_date}\n'
                f'{temperature}'
                f'({self._description})\n'
                f'{offset}Wind: '
                f'{self._wind} / Humidity: {self._humidity}\n')

from .unit import Unit


class UnitConverter:
    """
    The class constructor for the Unit Converter class. It makes conversions from Celsius to
    Fahrenheit and vice versa. Class initializer two arguments;
    1. the default unit used by the parser, and
    2. the destination unit.
    It has a dictionary containing the functions that will be used for temperature unit conversion.
    """
    def __init__(self,
                 parser_default_unit,
                 dest_unit=None):
        self._parser_default_unit = parser_default_unit
        self._dest_unit = dest_unit
        self._convert_functions = {
            Unit.CELSIUS: self._to_celsius,
            Unit.FAHRENHEIT: self._to_fahrenheit,
        }

    @property
    def dest_unit(self):
        """ The getter method for the destination temperature unit.
        :return: The destination unit
        """
        return self._dest_unit

    @dest_unit.setter
    def dest_unit(self, dest_unit):
        """ The setter method for the destination temperature unit.
        :param dest_unit: The temperature unit
        :return: None
        """
        self._dest_unit = dest_unit

    def convert(self, temp):
        """
        The convert method only gets one argument, the temperature. Here,
        the temperature is a string, so the first thing we do is try converting
        it to a float value; if it fails, it will return a zero value right away.
        It also verifies whether the destination unit is the same as the parser's
        default unit or not. If it is, it does not perform any conversion;
        it only formats the value and return it.
        :param temp: A string representation of a temperature.
        :return: The converted value
        """
        try:
            temperature = float(temp)
        except ValueError:
            return 0

        if self._dest_unit == self._parser_default_unit or self.dest_unit is None:
            return self._format_results(temperature)
        func = self._convert_functions[self._dest_unit]
        result = func(temperature)
        return self._format_results(result)

    @staticmethod
    def _format_results(value):
        """
        This function is a utility method that will format a given value. It checks if
        a value is an integer or a string - formatted as floating point with 1 precision.
        :param value: The temperature to be formatted.
        :return: The formatted value. Either as an int or floating point number with a precision of 1.
        """
        return int(value) if value.is_integer() else f'{value:.1f}'

    @staticmethod
    def _to_celsius(fahrenheit_temp):
        """
        This function converts a given temperature in fahrenheit and converts it to the
        equivalent celsius temperature.
        :param fahrenheit_temp:
        :return:
        """
        result = (fahrenheit_temp - 32) * 5 / 9
        return result

    @staticmethod
    def _to_fahrenheit(celsius_temp):
        """
        This function converts a given temperature in celsius and converts it to the
        equivalent fahrenheit temperature.
        :param celsius_temp:
        :return:
        """
        result = (celsius_temp * 9 / 5) + 32
        return result

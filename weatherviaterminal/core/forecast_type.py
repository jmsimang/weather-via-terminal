from enum import Enum, unique


@unique
class ForecastType(Enum):
    """
    This model represents all the information the application
    will scrape from the weather website.
    """
    TODAY = 'today'
    FIVEDAYS = '5day'
    TENDAYS = '10day'
    WEEKEND = 'weekend'

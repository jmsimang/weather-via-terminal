from enum import auto, unique
from .base_enum import BaseEnum

"""
Since the Unit class inherits from BaseEnum, every time the auto() is called,
the _generate_next_value_ method on BaseEnum will be invoked and will 
return the name of the property itself.
"""


@unique
class Unit(BaseEnum):
    """
    This class inherits from the BaseEnum, and every property is set to auto(). This means
    the value for every item in the enumeration will be set automatically.
    """
    CELSIUS = auto()
    FAHRENHEIT = auto()

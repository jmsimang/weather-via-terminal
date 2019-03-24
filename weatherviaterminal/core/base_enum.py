from enum import Enum

"""
 The only thing we want to do here is override the method _generate_next_value_ so that 
 every enumeration that inherits from BaseEnum and has properties with the value set to auto()
 will automatically get the same value as the property name.
"""


class BaseEnum(Enum):
    """
    An enumeration to represent the temperature units that the
    user will be able to choose from in the command line.
    """
    def _generate_next_value_(name, start, count, last_values):
        return name

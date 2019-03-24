import sys
from argparse import ArgumentParser


from weatherviaterminal.core import parser_loader
from weatherviaterminal.core import ForecastType
from weatherviaterminal.core import Unit
from weatherviaterminal.core import SetUnitAction


def _validate_forecast_args(args):
    if args.forecast_option is None:
        error_message = ('One of these arguments must be used: '
                         '-td/--today, -5d/--fivedays, -10d/--tendays, -'
                         'w/--weekend')
        print(f'{argparser.prog}: err: {error_message}',
              file=sys.stderr)
        sys.exit()


parsers = parser_loader.load('./weatherviaterminal/parsers')

argparser = ArgumentParser(
    prog='weatherviaterminal',
    description='Weather information from weather.com on your terminal'
)

required = argparser.add_argument_group('required arguments')
required.add_argument('-p', '--parser',
                      choices=parsers.keys(),
                      required=True,
                      dest='parser',
                      help=('Specify which parser is going to be'
                            'used to scrape weather information.'))

unit_values = [name.title() for name, value in Unit.__members__.items()]

required.add_argument('-u', '--unit',
                      choices=unit_values,
                      action=SetUnitAction,
                      required=False,
                      dest='unit',
                      help=('Specify the unit that will be used to display'
                            'the temperatures'))
required.add_argument('-a', '--areacode',
                      required=True,
                      dest='area_code',
                      help=('The code area to get the weather broadcast'
                            'from. It can be obtained at https://weather.com'))
argparser.add_argument('-v', '--version',
                       action='version',
                       version='%(prog)s 1.0')
argparser.add_argument('-td', '--today',
                       dest='forecast_option',
                       action='store_const',
                       const=ForecastType.TODAY,
                       help='Show the weather forecast for the current day')

args = argparser.parse_args()

_validate_forecast_args(args)

cls = parsers[args.parser]

parser = cls()
results = parser.run(args)

for result in results:
    print(results)

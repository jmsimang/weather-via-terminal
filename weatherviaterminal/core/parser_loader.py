import os
import re
import inspect


def _get_parser_list(dirname):
    """
    Function returns list of all files located in dirname. It filters files based on the rules of the
    parser.
    :param dirname: The location of parser files.
    :return: List of all files matching a condition of the file parser.
    """
    files = [f.replace('.py', '')
             for f in os.listdir(dirname)
             if not f.startswith('__')]
    return files


def _import_parsers(parserfiles):
    """
    Function imports the project modules, loop through the items in the module and extracts the parser classes,
    returning a dictionary containing the name of the class and the class object, which is used to create
    instances of the parser.
    :param parserfiles: Parser files to loop through.
    :return: A dictionary containing class names and objects.
    """
    m = re.compile('.+parser$', re.I)
    _modules = __import__('weatherterminal.parsers',
                          globals(),
                          locals(),
                          parserfiles,
                          0)
    _parsers = [(k, v) for k, v in inspect.getmembers(_modules)
                if inspect.ismodule(v) and m.match(k)]
    _classes = dict()
    for k, v in _parsers:
        _classes.update({k: v for k, v in inspect.getmembers(v)
                         if inspect.isclass(v) and m.match(k)})
    return _classes


def load(dirname):
    parserfiles = _get_parser_list(dirname)
    return _import_parsers(parserfiles)

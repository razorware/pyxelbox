import importlib

from os import path
from collections import namedtuple

from jargon_py import jargon
from jargon_py.query import *

TargetInfo = namedtuple('TargetInfo', 'module target')

MARKUP_EXT = ".jss"

__imports = {}


def get_import(name):
    if name not in __imports:
        return None

    return __imports[name]


def get_param(_class, node, param, **kwargs):
    """
    retrieves a parameter value from a node: e.g. "r:0 c:1 a:top-left"

    :param _class: class type to be initialized with the value

    :param node: node with parameters
    :type node: KeyNode

    :param param: parameter to be returned
    :type param: str

    :param kwargs: if function to be applied to value; ex. 'func': lambda v: func(v)
    :type kwargs: dict

    :return: value of type _class
    """
    if param in node:
        val = node[param]
    elif param in node.value:
        val = node.value[param]
    else:
        val = None

    if not val:
        #   TODO: raise exception ...???
        return val

    func = None
    if 'func' in kwargs:
        func = kwargs['func']

    return _class(val) if func is None else func(_class(val))


def load_markup(file, **kwargs):
    if 'module' in kwargs:
        file_path = path.dirname(kwargs['module'].__file__)
        file = path.join(file_path, file)

    return jargon.load(file)


def load_file_module(file):
    module_path = path.basename(path.dirname(file))
    markup = load_markup(file)
    name_parts = get_param(str, one(markup['application']), 't', func=lambda s: s.split('.'))

    target = '{mod}.{target}'.format(mod=module_path,
                                     target='.'.join(name_parts[:-1]))

    return importlib.import_module(target)


def load_reference(ref_module, ref_path):
    if isinstance(ref_module, str):
        path_parts = list(ref_module.split('.'))
    else:
        path_parts = list(ref_module.__name__.split('.'))

    path_parts += (ref_path.split('.'))

    ref_object = path_parts[-1]
    ref_module = '{module}'.format(module='.'.join(path_parts[:-1]))

    module = importlib.import_module(ref_module)

    return getattr(module, ref_object)


class Section:

    @property
    def name(self):
        return self.__name

    @property
    def nodes(self):
        return list(self.__iter__())

    def __init__(self, name, node):
        self.__name = name
        self.__node = node

    def __getitem__(self, item):
        if item in self.__node:
            return self.__node[item]

        return None

    def __iter__(self):
        if self.__node.value:
            value = self.__node.value
            if isinstance(value, dict):
                return iter((k, v) for k, v in value.items())
            elif isinstance(value, list):
                return iter(n for n in value)
            else:
                return iter(v for v in [value])

        return iter(n for n in self.__node.nodes)

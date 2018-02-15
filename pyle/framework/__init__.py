import json
import importlib

from os import path
from collections import namedtuple

TargetInfo = namedtuple('TargetInfo', 'module target')

MARKUP_EXT = ".json"

__imports = {}


def __get_sanitized_markup(data):
    markup = str()

    i = 0
    while i in range(0, len(data)):
        # check for comments
        if data[i:i+2] == '//':     # // ... EOL
            i += 2

            # move to EOL
            while i < len(data) and (data[i] != '\r' and data[i] != '\n'):
                if i == 180:
                    pass

                i += 1

            if i < len(data):
                if data[i] == '\r':
                    i += 1

                if data[i] == '\n':
                    i += 1

            continue

        elif data[i:i+2] == '/*':     # /* ... */
            i += 2

            # move to '*/'
            while i < len(data) and data[i:i+2] != '*/':
                i += 1

            i += 2
            if i < len(data):
                if data[i] == '\r':
                    i += 1

                if data[i] == '\n':
                    i += 1

            continue

        elif data[i] == '\r':
            i += 1

            continue

        elif data[i] == '\n':
            i += 1

            continue

        elif data[i] == '\t':
            i += 1

            continue

        else:
            markup += data[i]

        i += 1

    return markup


def sanitize_markup(**kwargs):
    data = None

    if 'source' in kwargs:
        data = kwargs['source']

    elif 'file' in kwargs:
        file = kwargs['file']

        if path.isfile(file):
            ext = path.splitext(file)

            if ext[1] != MARKUP_EXT:
                raise Exception('file [{file}] is not a JSON file: {ext}'
                                .format(file=file,
                                        ext=ext))

            with open(file) as j_markup:
                data = j_markup.read()

        else:
            raise FileExistsError('file [{file}] does not exist or is not a file'
                                  .format(file=file))

    return __get_sanitized_markup(data)


def get_import(name):
    if name not in __imports:
        return None

    return __imports[name]


def get_param(_class, pack_arr, param, **kwargs):
    """
    retrieves a parameter value from a packed parameter array: e.g. "r:0 c:1 a:top-left"

    :param _class: class type to be initialized with the value
    :param pack_arr: packed array string
    :param param: parameter to be returned
    :param kwargs: if function to be applied to value; ex. 'func': lambda v: func(v)

    :return: value of type _class
    """
    pack_arr = str(pack_arr)
    if param not in pack_arr:
        return None

    param += ':'        # add : to trail param label
    p_idx = pack_arr.find(param)
    # if ":" is immediately followed by "'" then we have a string value, e.g.: "n:'some string value'
    if pack_arr[p_idx+len(param)] == "'":
        p_idx = pack_arr.find("'", p_idx + len(param))
        p_end = pack_arr.find("'", p_idx + 1) + 1               # include trailing "'"
        val = pack_arr[p_idx:p_end] if p_end != -1 else None
    else:
        p_end = pack_arr.find(" ", p_idx + len(param))
        val = pack_arr[(p_idx + len(param)):p_end] if p_end != -1 else pack_arr[(p_idx + len(param)):]

    if val is None:
        #   TODO: raise exception ...???
        return val

    func = None
    if 'func' in kwargs:
        func = kwargs['func']

    return _class(val) if func is None else func(_class(val))


def load_markup(file):
    return json.loads(sanitize_markup(file=file))


def load_file_module(file):
    module_path = path.basename(path.dirname(file))
    markup = load_markup(file)
    name_parts = get_param(str, markup['application'], 't', func=lambda s: s.split('.'))
    target = '{mod}.{target}'.format(mod=module_path,
                                     target='.'.join(name_parts[:-1]))

    return importlib.import_module(target)

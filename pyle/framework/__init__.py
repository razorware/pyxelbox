import json

from os import path


MARKUP_EXT = ".json"


def __get_clean_markup(data):
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


def clean_markup(**kwargs):
    data = None

    if 'source' in kwargs:
        data = kwargs['source']

    elif 'file' in kwargs:
        fpath = kwargs['file']

        if path.isfile(fpath):
            ext = path.splitext(fpath)

            if ext[1] != MARKUP_EXT:
                raise Exception('file [{fpath}] is not a JSON file: {ext}'
                                .format(fpath=fpath,
                                        ext=ext))

            with open(fpath) as j_markup:
                data = j_markup.read()

        else:
            raise FileExistsError('file [{fpath}] does not exist or is not a file'
                                .format(fpath=fpath))

    return __get_clean_markup(data)


def load_markup(fpath):
    return json.loads(clean_markup(file=fpath))

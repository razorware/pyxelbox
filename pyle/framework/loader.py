import importlib

from os import path

from pyle.framework import get_param, \
    load_markup, \
    load_file_module, \
    load_reference, \
    Section

S_WINDOW = "Window"
S_GRID = "Grid"
S_RESOURCES = "Resources"
S_MENU = "Menu"


class Loader:

    @property
    def sections(self):
        return self.__sections

    @property
    def size(self):
        return {'width': self.__view_cnf['cnf']['width'],
                'height': self.__view_cnf['cnf']['height']}

    @property
    def title(self):
        return self.__view_cnf['title']

    @property
    def window(self):
        return self.__view_cnf['window']

    def __init__(self, view_info):
        """
        formerly: Controller

        Loader is responsible for loading the view markup and setting configurations
        to be used by the Renderer (formerly: LayoutManager).

        :param view_info: view info containing the views module and the target json
        markup

        :return:
        """
        markup = load_markup(view_info.target, module=view_info.module)
        self.__sections = []

        window = None

        for key in markup:
            section = Section(key, markup[key])

            if key == S_WINDOW:
                window = section

            self.__sections.append(section.name)

        # Window is the only required section
        if window is None:
            raise Exception("A " + S_WINDOW + " must be configured in json markup")

        self.__view_cnf = {
            'window': load_reference(view_info.module,
                                     window['class'][0]),
            'title': window['title'][0],
            'cnf': {}
        }

        if 'size' in window.keys():
            size = window['size'][0]
        else:
            #   default size
            size = "w:350 h:350"

        self.__view_cnf['cnf'].update({'width': get_param(int, size, 'w')})
        self.__view_cnf['cnf'].update({'height': get_param(int, size, 'h')})

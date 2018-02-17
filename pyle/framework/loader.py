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
    def children(self):
        return self.__children

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

        # 1: load sections
        window = self.__load_sections(markup)

        # 2: configure window -- Window is the only required section
        if window is None:
            raise Exception("A " + S_WINDOW + " must be configured in json markup")
        else:
            self.__configure_view(view_info, window)

        # 3: configure resources

        # 4: configure menu

        # 5: configure grid
        self.__children = {}
        if S_GRID in self.__sections:
            print('configuring children')
            self.__configure_children(markup[S_GRID])

    def run(self):
        window = self.window(cnf=self.__view_cnf['cnf'])
        window.master.title(self.__view_cnf['title'])

        window.master.mainloop()

    def __load_sections(self, markup):
        window = None

        for key in markup:
            section = Section(key, markup[key])

            if key == S_WINDOW:
                window = section

            self.__sections.append(section.name)

        return window

    def __configure_view(self, view_info, window):
        """

        :param view_info:
        :type view_info: TargetInfo

        :param window:
        :type window: Section

        :return:
        """
        self.__view_cnf = {
            'window': load_reference(view_info.module,
                                     window['class']),
            'title': window['title'],
            'cnf': {}
        }

        if 'size' in window:
            size = window['size']
        else:
            #   default size
            size = "w:350 h:350"

        self.__view_cnf['cnf'].update({'width': get_param(int, size, 'w')})
        self.__view_cnf['cnf'].update({'height': get_param(int, size, 'h')})

    def __configure_children(self, children):
        i = 0
        for ch in children:
            for k, v in ch.items():
                cls_child = load_reference('tkinter', k)
                name = '{cls}_{id}'.format(cls=cls_child.__name__, id=i)
                cls_info = {
                    "class": cls_child,
                    "cnf": v
                }

                self.__children.update({name: cls_info})

            i += 1

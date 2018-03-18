from os import path

from jargon_py.query import one

from pyle.framework import get_param, \
    load_markup, \
    load_file_module, \
    TargetInfo
from pyle.framework.loader import Loader


class Application:
    @property
    def name(self):
        return self.__app_cnf['name']

    @property
    def target(self):
        return self.__app_cnf['target']

    @property
    def views(self):
        return self.__app_cnf['views']

    def __init__(self, app_info):
        """
        Application loads the file containing json markup to initialize the application.

        :param app_info: application target information including the app module and name
        of the app's json markup file.

        :return:
        """
        markup = load_markup(app_info.target)
        self.__app_cnf = {
            'name': get_param(str, one(markup['application']), 'n', func=lambda s: s.replace("'", "")),
            'views': load_file_module(app_info.target)
        }
        self.__set_target_path(markup)

        self.mainloop = self.__run

    def __set_target_path(self, markup):
        views = self.__app_cnf['views']
        target_path = get_param(str, one(markup['application']), 't',
                                func=lambda s: '{dir}\\{file}.jss'.format(dir=path.dirname(views.__file__),
                                                                          file=s.split('.')[-1]))

        self.__app_cnf.update({'target': target_path})

    def __run(self):
        view_info = TargetInfo(self.__app_cnf['views'], self.__app_cnf['target'])
        loader = Loader(view_info)
        loader.run()

import tkinter as tk

from abc import ABC


class View(ABC):

    def __init__(self, **kwargs):
        if 'master' not in kwargs:
            self.master = tk.Tk()
        else:
            self.master = kwargs['master']
            del kwargs['master']

        self.__view_cnf = {} if 'view_cnf' not in kwargs else kwargs['view_cnf']
        self.__title = "Default Window" if 'title' not in self.__view_cnf else self.__view_cnf['title']

        cnf = None if 'cnf' not in self.__view_cnf else self.__view_cnf['cnf']
        self._on_before_initialize(cnf)
        self.__initialize(cnf)
        self._on_after_initialize()

    def activate(self, container):
        """
        Initialize view/window

        :param container:   ["Label": {
                              "text": 'Hello, World!',
                              "size": "w:50"}
                            ]
        :type container: list

        :return:
        """
        for child in container:
            for ctrl, cnf in child.items():
                print(ctrl)

                tk_cls = getattr(tk, ctrl)
                tk_obj = tk_cls(master=self.frame, **cnf)
                tk_obj.grid(row=0, column=0)

                # if tk_cls is tk.Label:
                #     text = None
                #
                #     if 'text' in cnf:
                #         text = cnf['text']
                #         del cnf['text']
                #
                #     control = tk_cls(master=self.frame, text=text, **cnf)
                #     control.grid(row=0, column=0)

                # cls_1 = tk_cls(master=self.frame, text='Hello', relief=tk.SUNKEN)
                # cls_1.grid(row=0, column=0)
                #

    def _on_before_initialize(self, kw_cnf):
        pass

    def _on_after_initialize(self):
        pass

    def __initialize(self, kw_cnf):
        self.master.title(self.__title)

        # size = '{w}x{h}'.format(w=kw_cnf['width'],
        #                         h=kw_cnf['height'])
        # del kw_cnf['width']
        # del kw_cnf['height']
        #
        # #self.master.geometry(size)

        if kw_cnf is not None:
            # test following:
            # highlightbackground="color", highlightcolor="color", highlightthickness=int
            # kw_cnf['highlightbackground'] = "blue"
            # kw_cnf['highlightcolor'] = "blue"
            # kw_cnf['highlightthickness'] = 1
            # kw_cnf['bd'] = 0

            self.master.columnconfigure(0, minsize=kw_cnf['width'])
            self.master.rowconfigure(0, minsize=kw_cnf['height'])
            self.frame = tk.Frame(master=self.master, **kw_cnf)
        else:
            self.frame = tk.Frame(master=self.master)

        self.frame.grid(row=0, column=0, sticky="news")

        # TODO: row & col configuration
        #   default: frame is 1x1 grid
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

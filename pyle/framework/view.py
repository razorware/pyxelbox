import tkinter as tk

from abc import ABC


class View(ABC, tk.Frame):

    def __init__(self, **kwargs):
        if 'master' not in kwargs:
            kwargs['master'] = tk.Tk()

        self.__initialize(kwargs)

    def _on_before_initialize(self, kw_cnf):
        pass

    def _on_after_initialize(self):
        pass

    def __initialize(self, kw_cnf):
        self._on_before_initialize(kw_cnf)

        tk.Frame.__init__(self, **kw_cnf)
        self.grid(row=0, column=0)

        self._on_after_initialize()

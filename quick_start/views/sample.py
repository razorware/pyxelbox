from pyle.framework.view import View


class Sample(View):

    def __init__(self, **kwargs):
        View.__init__(self, **kwargs)

    def _on_before_initialize(self, kw_cnf):
        print("initializing Sample")


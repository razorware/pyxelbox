import sys

from pyle.framework import load_markup
from pyle.bootstrap import Application

if __name__ == "__main__":
    file = sys.argv[1]
    markup = load_markup(file)

    app = Application(markup)
    app.mainloop()

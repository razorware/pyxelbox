import sys

from pyle.bootstrap import Application

if __name__ == "__main__":
    file = sys.argv[1]

    app = Application(file)
    app.mainloop()

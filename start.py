import sys

from FirstWindow import FirstWindow
from PyQt5.QtWidgets import *
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FirstWindow()
    win.show()
    sys.exit(app.exec_())
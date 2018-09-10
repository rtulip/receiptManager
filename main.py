from PyQt4 import QtGui
from ui.gui import gui
import sys

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    ui = gui()
    ui.show()
    
    sys.exit(app.exec_())
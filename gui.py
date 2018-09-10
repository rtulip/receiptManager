import sys
from PyQt4 import QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    btn = QtGui.QPushButton("Hello World", None)
    btn.show()
    sys.exit(app.exec_())
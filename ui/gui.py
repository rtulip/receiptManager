import sys
from PyQt4 import QtGui
from manager_ui import Ui_MainWindow


class gui(QtGui.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    
    
    sys.exit(app.exec_())
from PyQt4 import QtGui
from ui.gui import gui
import sys

class manager():
    
    def __init__(self):
        
        self.persons = {}
        self.receipts = {}
        
        self.ui = gui(self)
        self.ui.show()
        
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    manager = manager()
    
    sys.exit(app.exec_())